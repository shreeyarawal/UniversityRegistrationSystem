# University Registration System

A web-based Student, Course, and Enrollment Management System built with **Python, Flask, SQLite, HTML, and CSS**.

This project demonstrates Object-Oriented Programming (OOP), relational database design, and full-stack web development through a simple, interactive university registration platform.

## Project Overview

The University Registration System helps organize student information, manage academic courses, and track student enrollments.

Instead of entering data manually into a database, users can interact with a web interface to create and view records.

The application connects a Flask backend to a SQLite database and uses Python classes to represent the system's core entities.

## Key Features

### Student Management
- Register new students with their first name, last name, and email address.
- Automatically assign unique student IDs.
- Display all registered students.
- Prevent duplicate student email addresses.

### Course Management
- Create courses using a unique course code and credit value.
- Automatically assign course IDs.
- Display all available courses.

### Enrollment Management
- Enroll existing students in available courses.
- Automatically record registration dates.
- Display enrollment information alongside student names and course codes.
- Prevent duplicate enrollments in the same course.

### Interactive Web Interface
- Simple and organized user interface.
- Forms for student, course, and enrollment registration.
- Tables displaying current database records.
- Success and error messages for user actions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming and OOP |
| Flask | Web application framework |
| SQLite | Relational database |
| HTML | Website structure |
| CSS | Website styling |
| Git | Version control |
| GitHub | Source code hosting |

## Object-Oriented Programming

The application uses three core Python classes.

**Student Class — `student.py`**

Represents an individual student and stores:
- Student ID
- First name
- Last name
- Email address

**Course Class — `course.py`**

Represents an academic course and stores:
- Course ID
- Course code
- Credits

**Enrollment Class — `enrollment.py`**

Represents the relationship between a student and a course and stores:
- Enrollment ID
- Student ID
- Course ID
- Registration date

These classes provide a structured approach to organizing application data using OOP principles.

## Database Design

The system uses three related tables:

| Table | Role | Primary Key |
|---|---|---|
| Students | Parent | StudentID |
| Courses | Parent | CourseID |
| Enrollments | Child | EnrollmentID |

The `Enrollments` table contains two foreign keys:

- `StudentID` references `Students(StudentID)`.
- `CourseID` references `Courses(CourseID)`.

This creates a many-to-many relationship between students and courses through the Enrollments table.

A student can enroll in multiple courses, and a course can have multiple students.

## Project Structure

```text
UniversityRegistrationSystem/
│
├── app.py
├── student.py
├── course.py
├── enrollment.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

### File Descriptions

| File | Description |
|---|---|
| `app.py` | Main Flask application and routes |
| `student.py` | Student class |
| `course.py` | Course class |
| `enrollment.py` | Enrollment class |
| `database.py` | SQLite connection and table initialization |
| `templates/index.html` | Website interface |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes local and temporary files |

## Installation and Setup

### Prerequisites

Install Python 3 and Git on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/shreeyarawal/UniversityRegistrationSystem.git
cd UniversityRegistrationSystem
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Environment

For macOS or Linux:

```bash
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Website

Visit:

**http://127.0.0.1:5000**

The application initializes its SQLite database locally.

## How to Use

**Register a Student**

Enter a student's first name, last name, and email address, then click **Add Student**.

**Create a Course**

Enter a unique course code and the number of credits, then click **Add Course**.

**Enroll a Student**

Select an existing student and an available course, then click **Enroll Student**.

**View Records**

Scroll to the following sections:
- Show All Students
- Show All Courses
- Show All Enrollments

The application displays the stored records in organized tables.

## Screenshots

Screenshots of the working application can be added here to demonstrate:

- University Registration System homepage
- Student and course registration forms
- Student, course, and enrollment records
- Duplicate enrollment validation

## Validation and Testing

The application has been manually tested locally for the following operations:

- Successfully registering a student.
- Successfully creating a course.
- Successfully enrolling a student in a course.
- Retrieving and displaying stored records.
- Detecting and rejecting duplicate enrollments.

## Current Deployment Status

The application currently runs locally using Flask and SQLite.

Public hosting and a production database are planned as future improvements.

## Future Improvements

- Deploy the application to Vercel.
- Integrate a hosted PostgreSQL database.
- Improve responsive layouts for mobile devices.
- Add search and filtering features.
- Add edit and delete operations.
- Explore a React-based frontend.

## Academic Information

**Course:** MAC 250 — Database Management

**Project:** Student, Course, and Enrollment Management System

**Project Type:** Python OOP and Database Web Application

## Repository

GitHub: https://github.com/shreeyarawal/UniversityRegistrationSystem

---

*Developed as an academic project demonstrating Python, object-oriented design, relational databases, and web application development.*
