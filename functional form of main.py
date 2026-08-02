#how it is :
# main()
# │
# ├── show_menu()
# ├── process_choice()
# │   ├── add_student()
# │   ├── show_students()
# │   ├── delete_student()
# │   ├── ending_the_code()
# │   └── clear_screen()
# │
# ├── save_data()
# └── load_data()

#کتابخانه های مورد استفاده
import os
import time
from tqdm import tqdm
import json
from pathlib import Path


#سیو اظلاعات توی فایل جیسون
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "database" / "students.json"

if JSON_PATH.exists():
   with open(JSON_PATH, "r") as file:
    Student_data = json.load(file)
else:
    Student_data = []



#توابع فرعی
def save_data():
    with open(JSON_PATH, "w") as file:
        json.dump(Student_data, file )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ending_the_code():
   answer_input = input("do you want to back to the list of options?(y/n)")
   if answer_input.upper() in ["YES", "BALE", "Y"]:
        return True
   else:
    print("Good Bye😒")
          





#توابع اصلی
def show_menu():
    print("""
    ======= Student Management ======
    1. Add student
    2. Show student list
    3. Delete student
    4. Exit
    """)

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    student = {
        "name": name,
        "age": age
    }

    Student_data.append(student)
    save_data()


def show_students():
    counter = 0
    for student in Student_data:
        counter += 1
        print(f"{counter}: {student}")


def delete_student():
    show_students()   
    choose = int(input("which student : "))     
    delete = Student_data[choose-1]
    Student_data.remove(delete)
    save_data()

def process_choice(choice):
    if choice == 1:
        add_student()

    elif choice == 2:
        show_students()

    elif choice == 3:
        delete_student()

    elif choice == 4:
        print("Good Bye😒")
        return False

    

def main():
    while True:
        try:
            show_menu()
            choice = int(input("Enter your option: "))
            process_choice(choice)
            if not ending_the_code():
             break
            clear_screen()


        except (ValueError,IndexError):
            print("""============= Error 🚨==============
                    
                       =====just enter a number between 1_4=====
                    
                 =============== try again after 10 second =============
                    """)
            
            for i in tqdm(range(10)):
                time.sleep(1)
                continue
            clear_screen()



main()

