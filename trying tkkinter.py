#made halfly by ai





#کتابخانه های مورد استفاده
import json
from pathlib import Path
from tkinter import *
from tkinter import messagebox

#سیو اظلاعات توی فایل جیسون
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "database" / "students.json"

if JSON_PATH.exists():
   with open(JSON_PATH, "r") as file:
    Student_data = json.load(file)
else:
    Student_data = []


#تابع سیو مقادیر
def save_data():
    with open(JSON_PATH, "w") as file:
        json.dump(Student_data, file, indent=4)

#قسمت اصلی کد 
class App(Tk):

    def __init__(self):
        super().__init__()

        self.title("Student Management")
        self.geometry("500x500")

        Label(
            self,
            text="Student Management System",
            font=("Tahoma", 18, "bold")
        ).pack(pady=40)

        #لیست موارد

        self.frame = Frame(self)
        self.frame.pack()

        Button(
            self.frame,
            text="Add Student",
            width=20,
            command=self.show_add_form
        ).pack(pady=5)

        Button(
            self.frame,
            text="Show Students",
            width=20,
            command=self.show_student_list
        ).pack(pady=5)

        Button(
            self.frame,
            text="Delete Student",
            width=20,
            command=self.show_delete_list
        ).pack(pady=5)

        Button(
            self.frame,
            text="Exit",
            width=20,
            command=self.destroy
        ).pack(pady=5)


        self.add_frame = Frame(self)

        Label(
            self.add_frame,
            text="Student Name"
        ).pack()

        self.name_entry = Entry(
            self.add_frame,
            width=30
        )

        self.name_entry.pack(pady=5)

        Label(
            self.add_frame,
            text="Student Age"
        ).pack()

        self.age_entry = Entry(
            self.add_frame,
            width=30
        )

        self.age_entry.pack(pady=5)

        Button(
            self.add_frame,
            text="Save",
            command=self.add_student
        ).pack(pady=5)

        Button(
            self.add_frame,
            text="Back",
            command=self.back_to_menu
        ).pack()


        self.show_frame = Frame(self)

        self.show_listbox = Listbox(
            self.show_frame,
            width=45,
            height=12
        )

        self.show_listbox.pack(pady=10)

        Button(
            self.show_frame,
            text="Back",
            command=self.back_to_menu
        ).pack()


        self.delete_frame = Frame(self)

        self.delete_listbox = Listbox(
            self.delete_frame,
            width=45,
            height=12
        )

        self.delete_listbox.pack(pady=10)

        Button(
            self.delete_frame,
            text="Delete",
            command=self.delete_student
        ).pack(pady=5)

        Button(
            self.delete_frame,
            text="Back",
            command=self.back_to_menu
        ).pack()


    def back_to_menu(self):

        self.add_frame.pack_forget()
        self.show_frame.pack_forget()
        self.delete_frame.pack_forget()

        self.frame.pack()


    def show_add_form(self):

        self.back_to_menu()

        self.frame.pack_forget()

        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)

        self.add_frame.pack(pady=20)


    def add_student(self):

        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if name == "" or age == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number.")
            return

        Student_data.append({
            "name": name,
            "age": age
        })

        save_data()

        messagebox.showinfo("Success", "Student added successfully.")

        self.back_to_menu()


    def show_student_list(self):

        self.back_to_menu()

        self.frame.pack_forget()

        self.show_listbox.delete(0, END)

        if len(Student_data) == 0:
            self.show_listbox.insert(END, "No students found.")
        else:
            for i, student in enumerate(Student_data, start=1):
                self.show_listbox.insert(
                    END,
                    f"{i}. {student['name']}   Age : {student['age']}"
                )

        self.show_frame.pack(pady=20)


    def show_delete_list(self):

        self.back_to_menu()

        self.frame.pack_forget()

        self.delete_listbox.delete(0, END)

        if len(Student_data) == 0:
            self.delete_listbox.insert(END, "No students found.")
        else:
            for i, student in enumerate(Student_data, start=1):
                self.delete_listbox.insert(
                    END,
                    f"{i}. {student['name']}   Age : {student['age']}"
                )

        self.delete_frame.pack(pady=20)

    
    def delete_student(self):

        selected = self.delete_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a student."
            )
            return

        index = selected[0]

        answer = messagebox.askyesno(
            "Delete",
            "Delete this student?"
        )

        if answer:

            Student_data.pop(index)

            save_data()

            messagebox.showinfo(
                "Done",
                "Student deleted successfully."
            )

            self.show_delete_list()


if __name__ == "__main__":
    app = App()
    app.mainloop()