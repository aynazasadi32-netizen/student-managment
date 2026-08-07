import time
from tqdm import tqdm
from database.save_load import Student_data, save_data


def delete_student():
    counter = 0    

    for student in Student_data:
        counter += 1
        print(f"{counter}: {student}")  

    try:
        choose = int(input("which student : "))     
        delete = Student_data[choose - 1]
        Student_data.remove(delete)
        save_data()

    except:
        print("Invalid student number. try again after 3 second")

        for i in tqdm(range(3)):
            time.sleep(1)
