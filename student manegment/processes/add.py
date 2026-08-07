from save_load import Student_data, save_data


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    student = {
        "name": name,
        "age": age
    }

    Student_data.append(student)
    save_data()
