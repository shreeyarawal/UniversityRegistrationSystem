
import sqlite3

DATABASE_NAME = "university.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    with get_connection() as connection:
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                FirstName VARCHAR(50) NOT NULL,
                LastName VARCHAR(50) NOT NULL,
                Email VARCHAR(100) UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Courses (
                CourseID INTEGER PRIMARY KEY,
                CourseCode VARCHAR(10) UNIQUE NOT NULL,
                Credits INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Enrollments (
                EnrollmentID INTEGER PRIMARY KEY,
                StudentID INTEGER NOT NULL,
                CourseID INTEGER NOT NULL,
                RegistrationDate DATETIME NOT NULL,

                FOREIGN KEY (StudentID)
                    REFERENCES Students(StudentID),

                FOREIGN KEY (CourseID)
                    REFERENCES Courses(CourseID)
            );
        """)
