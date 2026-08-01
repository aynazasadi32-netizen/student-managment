import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "database" / "students.json"

with open(JSON_PATH, "r") as file:
    Student_data = json.load(file)

def save_data():
    with open(JSON_PATH, "w") as file:
        json.dump(Student_data, file, indent=4)

while True :
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
        with open("students.json", "w") as file:
                json.dump(Student_data, file, indent=4)
        save_data()
          

    
    elif choose == 2 :
         conter = 0
         for i in Student_data:
             conter+=1
             print(f"{conter} : {i}") 
             

        
    elif choose == 3 :
        choose = int(input("which student : "))
        delete = Student_data[choose-1]
        Student_data.remove(delete)
       
        save_data()            
    
    
    elif choose == 4:
        print("Good Bye😒")
        break


