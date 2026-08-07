import time
from tqdm import tqdm

from add import add_student
from show import show_students
from delete import delete_student


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

    else:
        print("""
============= Error 🚨==============

Just enter a number between 1 and 4.

Try again after 3 seconds.
""")

        for _ in tqdm(range(3)):
            time.sleep(1)
