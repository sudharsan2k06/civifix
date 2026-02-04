import sqlite3
from datetime import datetime

DB_NAME = "civic_reporter.db"


# ---------- DATABASE CONNECTION ----------
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- CREATE TABLE ----------
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue_type TEXT NOT NULL,
        description TEXT,
        latitude REAL,
        longitude REAL,
        image_path TEXT,
        status TEXT DEFAULT 'Pending',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# ---------- INSERT COMPLAINT ----------
def insert_complaint(issue_type, description, latitude, longitude, image_path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO complaints (
        issue_type,
        description,
        latitude,
        longitude,
        image_path,
        status,
        created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        issue_type,
        description,
        latitude,
        longitude,
        image_path,
        "Pending",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# ---------- GET ALL COMPLAINTS ----------
def get_all_complaints():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM complaints
    ORDER BY created_at DESC
    """)

    complaints = cursor.fetchall()
    conn.close()
    return complaints


# ---------- GET DASHBOARD COUNTS ----------
def get_status_counts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM complaints")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status = 'Pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status = 'In Progress'")
    progress = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status = 'Resolved'")
    resolved = cursor.fetchone()[0]

    conn.close()
    return total, pending, progress, resolved


# ---------- UPDATE STATUS (ADMIN) ----------
def update_complaint_status(complaint_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE complaints
    SET status = ?
    WHERE id = ?
    """, (new_status, complaint_id))

    conn.commit()
    conn.close()
