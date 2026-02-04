# 🏙️ Smart Civic Issues Reporter (AI-Powered)

An AI-powered civic issue reporting system that enables citizens to report road potholes and broken streetlights using image-based detection and automatic location mapping.

---

## 📌 Problem Statement

Urban civic issues such as potholes and broken streetlights often remain unresolved due to:
- Manual complaint processes
- Inaccurate location details
- Lack of visual proof
- Delayed response from authorities

This project addresses these challenges by using **Artificial Intelligence + Geolocation** to automate and streamline civic issue reporting.

---

## 🚀 Solution Overview

The system allows users to:
- Capture or upload images of civic issues
- Automatically detect the issue type using a pre-trained ML model
- Capture GPS coordinates and convert them into a readable address
- Submit verified reports to a centralized system for authorities

The focus is on **accuracy, reliability, and real-world usability**, keeping the UI minimal and efficient.

---

## ✨ Key Features

- 📷 **Image-Based Issue Detection**
  - Detects potholes and broken streetlights using a trained ML model

- 📍 **Automatic Location Capture**
  - Captures latitude & longitude
  - Converts coordinates into a human-readable address

- 🗂️ **Issue Categorization**
  - Automatic classification based on AI prediction

- 🗺️ **Map-Based Visualization**
  - Displays reported issues on an interactive map

- 🕒 **Real-Time Reporting**
  - Issues are stored instantly with timestamp and location

- 🛠️ **Admin / Authority Dashboard**
  - View, filter, and manage reported issues
  - Track issue status (Reported / In Progress / Resolved)

- 🔁 **Duplicate Issue Prevention**
  - Prevents multiple reports of the same issue in a nearby location

---

## 🧠 Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python (Flask / FastAPI)
- REST APIs

### Machine Learning
- Python
- Pre-trained Image Classification Model
- mobilenetv2
- TensorFlow 

### Database
- MongoDB / SQL (based on implementation)

### APIs & Services
- Geolocation API
- Reverse Geocoding API (Lat/Long → Address)
- Map API (Google Maps / OpenStreetMap)

---

## 🏗️ System Architecture

1. User captures or uploads an image
2. Image is sent to the backend
3. ML model predicts the issue type
4. Location is captured and converted to an address
5. Report is stored in the database
6. Issues are displayed on the admin dashboard and map view

---

## 🎯 Use Cases

- Smart city governance
- Municipal corporation issue tracking
- Citizen participation platforms
- Urban infrastructure monitoring

---

## 📈 Future Enhancements

- Add more civic issue categories (garbage, water leakage, road cracks)
- Severity detection using AI
- Notification system for users
- Heatmap analytics for authorities
- Government system API integration

---

## 🏆 Why This Project Matters

This project demonstrates:
- Real-world problem solving
- Practical application of AI
- End-to-end system development
- Smart city and civic-tech relevance

---

## 👨‍💻 Team

- Project developed as part of a hackathon / academic project  
- Focused on functionality, accuracy, and scalability

---

## 📄 License

This project is for educational and demonstration purposes.
