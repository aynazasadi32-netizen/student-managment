import time
from tqdm import tqdm

from utils import clear_screen
from processes.process import process_choice
from show_menu import show_menu

def main():
    while True:
        try:
            show_menu()
            choice = int(input("Enter your option: "))
            result = process_choice(choice)
            
            if result is False:
                break

            clear_screen()

        except:
            print("""============= Error 🚨==============
                    
                       =====just enter a number between 1_4=====
                    
                 =============== try again after 10 second =============
                    """)
            
            for i in tqdm(range(10)):
                time.sleep(1)
                continue

            clear_screen()


if __name__ == "__main__":
    main()
