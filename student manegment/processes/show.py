import time
from tqdm import tqdm
from save_load import Student_data


def show_students():
    counter = 0
    print("this list will be disapeard after 10 second")    
    
    for student in Student_data:
        counter += 1
        print(f"{counter}: {student}")

    for i in tqdm(range(10)):
        time.sleep(1)
