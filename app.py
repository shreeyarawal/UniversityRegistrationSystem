
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

from database import get_connection, create_tables
from student import Student
from course import Course
from enrollment import Enrollment

app = Flask(__name__)
app.secret_key = "university-registration-local-demo"

create_tables()


@app.route("/")
def index():
    with get_connection() as connection:
        students = connection.execute(
            "SELECT * FROM Students ORDER BY StudentID"
        ).fetchall()

        courses = connection.execute(
            "SELECT * FROM Courses ORDER BY CourseID"
        ).fetchall()

        enrollments = connection.execute("""
            SELECT e.EnrollmentID, s.FirstName, s.LastName,
                   c.CourseCode, e.RegistrationDate
            FROM Enrollments e
            JOIN Students s ON e.StudentID = s.StudentID
            JOIN Courses c ON e.CourseID = c.CourseID
            ORDER BY e.EnrollmentID
        """).fetchall()

    return render_template(
        "index.html",
        students=students,
        courses=courses,
        enrollments=enrollments
    )


@app.route("/add_student", methods=["POST"])
def add_student():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip()

    if not first_name or not last_name or not email:
        flash("Please complete all student fields.", "error")
        return redirect(url_for("index"))

    student = Student(None, first_name, last_name, email)

    try:
        with get_connection() as connection:
            connection.execute(
                """INSERT INTO Students (FirstName, LastName, Email)
                   VALUES (?, ?, ?)""",
                (student.first_name, student.last_name, student.email)
            )
        flash("Student added successfully!", "success")
    except sqlite3.IntegrityError:
        flash("That student email is already registered.", "error")

    return redirect(url_for("index"))


@app.route("/add_course", methods=["POST"])
def add_course():
    course_code = request.form["course_code"].strip().upper()

    try:
        credits = int(request.form["credits"])
        if not course_code or not 1 <= credits <= 6:
            raise ValueError

        course = Course(None, course_code, credits)

        with get_connection() as connection:
            connection.execute(
                "INSERT INTO Courses (CourseCode, Credits) VALUES (?, ?)",
                (course.course_code, course.credits)
            )

        flash("Course added successfully!", "success")
    except ValueError:
        flash("Enter a course code and credits from 1 to 6.", "error")
    except sqlite3.IntegrityError:
        flash("That course code already exists.", "error")

    return redirect(url_for("index"))


@app.route("/enroll", methods=["POST"])
def enroll():
    try:
        student_id = int(request.form["student_id"])
        course_id = int(request.form["course_id"])

        with get_connection() as connection:
            existing = connection.execute(
                """SELECT EnrollmentID FROM Enrollments
                   WHERE StudentID = ? AND CourseID = ?""",
                (student_id, course_id)
            ).fetchone()

            if existing:
                flash("Student is already enrolled in this course.", "error")
                return redirect(url_for("index"))

            enrollment = Enrollment(
                None, student_id, course_id,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            connection.execute(
                """INSERT INTO Enrollments
                   (StudentID, CourseID, RegistrationDate)
                   VALUES (?, ?, ?)""",
                (enrollment.student_id, enrollment.course_id,
                 enrollment.registration_date)
            )

        flash("Student enrolled successfully!", "success")
    except (ValueError, KeyError, sqlite3.IntegrityError):
        flash("Please select a valid student and course.", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
