from flask import Flask, render_template, request,redirect,url_for,Response
import os
import csv
from model import predict_issue
from db import init_db, insert_complaint, get_all_complaints,update_complaint_status
from db import get_status_counts


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize DB ONCE
init_db()

@app.route("/")
def home():
    return render_template("index.html")
##this ^ is admin dash board pade route!!!@
@app.route("/admin")
def admin():
    complaints = get_all_complaints()
    return render_template("adminpool.html", complaints=complaints)

@app.route("/report", methods=["GET"])
def report_form():
    return render_template("report.html")

@app.route("/report_submit", methods=["POST"])
def report_submit():
    description = request.form.get("description")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    image = request.files["image"]

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    issue_type = predict_issue(image_path)
    insert_complaint(
        issue_type,
        description,
        latitude,
        longitude,
        image_path
    )
    return redirect(url_for("success"))

@app.route("/user_dashboard")
def user_dashboard():
    complaints = get_all_complaints()

  #"""using default values ti avoid problem in userDA"""

    total_count = 0
    pending_count = 0
    progress_count = 0
    resolved_count = 0

    if complaints:
        total_count, pending_count, progress_count, resolved_count = get_status_counts()

    return render_template(
        "user-dashboard.html",
        complaints=complaints,
        total_count=total_count,
        pending_count=pending_count,
        progress_count=progress_count,
        resolved_count=resolved_count
    )


@app.route("/success")
def success():
    issue = request.args.get("issue", "unknown")
    return render_template("success.html")

##user login route
@app.route("/login")
def user_login():
    return render_template("user-login.html")
#singup raoutee
@app.route("/signup")
def user_signup():
    return render_template("signup-page.html")

@app.route("/adminlogin")
def admin_login():
    return render_template("admin-login.html")

#(feature bro)paaru  
@app.route("/export_csv")
def export_csv():
    complaints = get_all_complaints()

    def generate():
        yield "id,issue_type,latitude,longitude,status,created_at\n"
        for c in complaints:
            yield f"{c['id']},{c['issue_type']},{c['latitude']},{c['longitude']},{c['status']},{c['created_at']}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=civic_issues.csv"
        }
    )

@app.route("/update_status", methods=["POST"])
def update_status():
    complaint_id = request.form.get("complaint_id")
    new_status = request.form.get("status")
    
    if complaint_id and new_status:
        update_complaint_status(complaint_id, new_status)
        return redirect(url_for("admin"))
    return "Invalid request", 400



if __name__ == "__main__":
    app.run(debug=True)
