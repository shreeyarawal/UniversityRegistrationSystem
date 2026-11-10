
class Course:
    def __init__(self, course_id, course_code, credits):
        self.course_id = course_id
        self.course_code = course_code
        self.credits = credits

    def __str__(self):
        return (
            f"Course ID: {self.course_id}, "
            f"Course Code: {self.course_code}, "
            f"Credits: {self.credits}"
        )
