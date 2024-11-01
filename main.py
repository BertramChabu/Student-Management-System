class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    # methhod to add new student into the system

    def add_student(self, student):
        self.students[student.student_id] = student
        print(f"Student {student.name} added successfully.")
    # method to remove student from the list
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed successfully.")
        else:
            print("Student not found.")
    # update student deatils method
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print(f"Student with ID {student_id} updated successfully.")
        else:
            print("Student not found.")

    def view_student(self, student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found.")

    def list_students(self):
        for student in self.student.values():
            print(student)
        else:
            print("No student found in the system")
            


