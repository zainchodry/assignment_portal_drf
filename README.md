# 🎓 Assignment Management System (Django REST Framework)

## 📘 Overview
The **Assignment Management System** is a Django REST Framework (DRF)-based backend that allows:
- Students to view and submit assignments.
- Instructors to create, update, and grade assignments.
- Secure authentication for users (students and instructors).

This project follows a modular architecture with separate apps:
- **accounts** → Handles user registration, login, and authentication.
- **courses** → Manages course creation and enrollment.
- **assignments** → Handles assignment creation, submission, and grading.

---

## 🏗️ Project Structure

```
assignment_system/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── courses/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── assignments/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── assignment_system/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Features

### 👨‍🏫 For Instructors
- Create and manage courses
- Create assignments for each course
- View submissions from students
- Grade submissions

### 🎓 For Students
- View available assignments
- Submit assignment files
- View grades and feedback

---

## 🧩 Technologies Used
- **Python 3.8+**
- **Django 4.x**
- **Django REST Framework**
- **SQLite3 (default, can switch to PostgreSQL)**

---

## 🚀 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/zainchodry/assignment_portal_drf.git
cd assignment_portal_drf
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the server
```bash
python manage.py runserver
```

---

## 🔐 API Endpoints

### 🧾 Authentication (Accounts App)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/register/` | Register a new user |
| POST | `/api/login/` | Login user and get token |
| POST | `/api/logout/` | Logout user |

### 📚 Courses
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/courses/` | List all courses |
| POST | `/api/courses/` | Create a new course |
| GET | `/api/courses/<id>/` | Retrieve course details |
| PUT | `/api/courses/<id>/` | Update course |
| DELETE | `/api/courses/<id>/` | Delete course |

### 📝 Assignments
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/assignments/` | List all assignments |
| POST | `/api/assignments/` | Create a new assignment |
| GET | `/api/assignments/<id>/` | Retrieve assignment details |
| POST | `/api/assignments/<id>/submit/` | Submit an assignment |
| GET | `/api/submissions/` | View submitted assignments |

---

## 📁 Folder Explanation

| Folder | Description |
|--------|-------------|
| `accounts/` | User authentication logic (registration, login, logout) |
| `courses/` | Course management (CRUD APIs) |
| `assignments/` | Assignment and submission handling |
| `assignment_system/` | Project configuration and settings |

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author
**Developed by Zain Choudry**