
class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Name: {self.get_full_name()}, "
            f"Email: {self.email}"
        )
