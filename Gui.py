import tkinter as tk
from tkinter import messagebox
from main import Student, StudentManagementSystem

class StudentManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.system = StudentManagementSystem()

        # Student ID label and input
        tk.Label(root, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
        self.student_id_entry = tk.Entry(root)
        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Name label and input
        tk.Label(root, text="Name").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Age label and input
        tk.Label(root, text="Age",).grid(row=2, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        # Major label and input
        tk.Label(root, text="Major").grid(row=3, column=0, padx=5, pady=5)
        self.major_entry = tk.Entry(root)
        self.major_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_student).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(root, text="Update Student", command=self.update_student).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(root, text="View Student", command=self.view_student).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(root, text="List Students", command=self.list_students).grid(row=5, column=1, padx=5, pady=5)

        # Output Display
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_student(self):
        try:
            student_id = int(self.student_id_entry.get())
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            major = self.major_entry.get()
            student = Student(student_id, name, age, major)
            self.system.add_student(student)
            messagebox.showinfo("Success", "Student added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your data.")

    def update_student(self):
        try:
            student_id = int(self.student_id_entry.get())
            name = self.name_entry.get() or None
            age = int(self.age_entry.get()) if self.age_entry.get() else None
            major = self.major_entry.get() or None
            self.system.update_student(student_id, name, age, major)
            messagebox.showinfo("Success", "Student updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your data.")

    def view_student(self):
        try:
            student_id = int(self.student_id_entry.get())
            student = self.system.students.get(student_id)
            self.output_text.delete(1.0, tk.END)
            if student:
                self.output_text.insert(tk.END, str(student) + "\n")
            else:
                self.output_text.insert(tk.END, "Student not found.\n")
        except ValueError:
            messagebox.showerror("Error", "Invalid Student ID")

    def list_students(self):
        self.output_text.delete(1.0, tk.END)
        if self.system.students:
            for student in self.system.students.values():
                self.output_text.insert(tk.END, str(student) + "\n")
        else:
            self.output_text.insert(tk.END, "No students to display.\n")

# Main GUI loop
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()
