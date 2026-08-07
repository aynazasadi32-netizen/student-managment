# 🎓 Student Management System

A simple but structured **Student Management System** built with Python.

This project is created as a learning project to practice Python programming concepts, software structure, clean code, and basic Object-Oriented Programming.

The project starts from a simple Python script and gradually evolves into a structured application.

---

# 🚀 Features

Current features:

- ✅ Add new students
- ✅ Show all students
- ✅ Search students
- ✅ Delete students
- ✅ Update student information
- ✅ Save data permanently using JSON
- ✅ Load data automatically when application starts
- ✅ Input validation
- ✅ Clean project structure
- ✅ Object-Oriented Programming structure


---

# 🏗 Project Architecture
student_management/
│
├── main.py
│
├── config.py
│
├── database/
│   └── students.json
│
├── models/
│   └── student.py
│
├── services/
│   └── student_service.py
│
├── utils/
│   ├── validator.py
│   └── helper.py
│
└── README.md



project/
├── main.py
├── show_menu.py
├── save_load.py
├── utils.py
├── database/
│   └── students.json
└── process_choices/
    ├── __init__.py
    ├── process_choice.py
    ├── add_student.py
    ├── show_students.py
    └── delete_student.py
