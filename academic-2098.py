class Course:
    def __init__(self, course_code, course_name, credit_hours, course_description):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.course_description = course_description
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_course_details(self):
        course_details = f"Course Code: {self.course_code}\n"
        course_details += f"Course Name: {self.course_name}\n"
        course_details += f"Credit Hours: {self.credit_hours}\n"
        course_details += f"Course Description: {self.course_description}\n"
        return course_details

    def get_enrolled_students(self):
        enrolled_students = [student for student in self.students]
        return enrolled_students

# Create a course instance
course1 = Course("CS101", "Introduction to Computer Science", 3, "An introduction to the fundamentals of computer science.")

# Add students
course1.add_student("John Doe")
course1.add_student("Jane Smith")

# Remove a student
course1.remove_student("John Doe")

# Get course details
print(course1.get_course_details())

# Get enrolled students
enrolled_students = course1.get_enrolled_students()
print(enrolled_students)
