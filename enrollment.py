
class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, registration_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.registration_date = registration_date

    def __str__(self):
        return (
            f"Enrollment ID: {self.enrollment_id}, "
            f"Student ID: {self.student_id}, "
            f"Course ID: {self.course_id}, "
            f"Registration Date: {self.registration_date}"
        )
