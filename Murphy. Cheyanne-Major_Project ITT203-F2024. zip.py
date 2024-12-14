Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Course:
...     def __init__(self, course_id, name, fee):
...         self.course_id = course_id
...         self.name = name
...         self.fee = fee
... 
... class Student:
...     def __init__(self, student_id, name, email):
...         self.student_id = student_id
...         self.name = name
...         self.email = email
...         self.courses = []  # List of enrolled courses
...         self.balance = 0
... 
...     def enroll(self, course):
...         if course.course_id in [c.course_id for c in self.courses]:
...             raise ValueError(f"Student is already enrolled in course {course.course_id}.")
...         self.courses.append(course)
...         self.balance += course.fee
... 
...     def get_total_fee(self):
...         return sum(course.fee for course in self.courses)
... 
... class RegistrationSystem:
...     def __init__(self):
...         self.courses = []  # List of all available courses
...         self.students = {}  # Dictionary of student_id -> Student objects
... 
...     def add_course(self, course_id, name, fee):
...         if course_id in [course.course_id for course in self.courses]:
...             raise ValueError(f"Course ID {course_id} already exists.")
...         self.courses.append(Course(course_id, name, fee))
... 
...     def register_student(self, student_id, name, email):
...         if student_id in self.students:
...             raise ValueError(f"Student ID {student_id} is already registered.")
        self.students[student_id] = Student(student_id, name, email)

    def enroll_in_course(self, student_id, course_id):
        student = self.students.get(student_id)
        if not student:
            raise ValueError(f"Student ID {student_id} not found.")

        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            raise ValueError(f"Course ID {course_id} not found.")

        student.enroll(course)

    def calculate_payment(self, student_id, payment_amount):
        student = self.students.get(student_id)
        if not student:
            raise ValueError(f"Student ID {student_id} not found.")

        if payment_amount < 0.4 * student.balance:
            raise ValueError("Payment must be at least 40% of the balance.")

        student.balance -= payment_amount

    def check_student_balance(self, student_id):
        student = self.students.get(student_id)
        if not student:
            raise ValueError(f"Student ID {student_id} not found.")
        return student.balance

    def show_courses(self):
        return [(course.course_id, course.name, course.fee) for course in self.courses]

    def show_registered_students(self):
        return [(student.student_id, student.name, student.email) for student in self.students.values()]

    def show_students_in_course(self, course_id):
        course_students = [
            student.name
            for student in self.students.values()
            if course_id in [c.course_id for c in student.courses]
        ]
        return course_students

# Example usage
if __name__ == "__main__":
    system = RegistrationSystem()

    # Adding courses
    system.add_course("C101", "Math 101", 500)
    system.add_course("C102", "History 101", 300)

    # Registering students
    system.register_student("S001", "John Doe", "john@example.com")
    system.register_student("S002", "Jane Smith", "jane@example.com")

    # Enrolling students in courses
    system.enroll_in_course("S001", "C101")
    system.enroll_in_course("S002", "C102")

    # Making payments
    system.calculate_payment("S001", 200)

    # Checking balances
    print("John's balance:", system.check_student_balance("S001"))

    # Viewing details
    print("Courses:", system.show_courses())
    print("Registered Students:", system.show_registered_students())
    print("Students in Math 101:", system.show_students_in_course("C101"))
