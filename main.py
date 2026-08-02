#کتابخونه هایی که استفاده کردیم
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


#توابع (سیو،پاک کردن قبلی ها،پایان اجرا)
def save_data():
    with open(JSON_PATH, "w") as file:
        json.dump(Student_data, file )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ending_the_code():
    answer_input = input("Do you want to go back to the list of options? ")

    if answer_input.upper() in ["YES", "BALE", "Y"]:
        return True
    else:
        print("Good Bye😒")
          


#اصل کد
while True :
 try:
    print("""
       ======= Student Managment ====
        1 Add student 
        2 Show student list 
        3 delet student
        4 Exit    
    """)
    choose = int(input("Enter your option : "))

    if choose == 1 :
        name = input("Enter student name : ")
        age = input("Enter student age : ")
        add = {
            "name":name,
            "age" : age
            }
        
        Student_data.append(add)
        save_data()
        if not ending_the_code():
            break
        clear_screen()

    
    elif choose == 2 :
         conter = 0
         for student in Student_data:
             conter+=1
             print(f"{conter} : {student}") 
         if not ending_the_code():
            break
         clear_screen()    

        
    elif choose == 3 :
        conter = 0
        for i in Student_data:
            conter+=1
            print(f"{conter} : {i}")   
        choose = int(input("which student : "))     
        delete = Student_data[choose-1]
        Student_data.remove(delete)

    
        save_data() 
        if not ending_the_code():
         break
        clear_screen()
    
    elif choose == 4:
        print("Good Bye😒")
        break


 except:
        
        print("""============= Error 🚨==============
        
           =====just enter a number between 1_4=====
        
     =============== try again after 10 second =============
        """)

        for i in tqdm(range(10)):
            time.sleep(1)
            continue
        clear_screen()

    