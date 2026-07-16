#step 1: get current date for file name
#step 2: open file w date name and user input there
#step 3: command line interface
#step 4: go bullshit

from datetime import datetime
import pathlib
import sys
def main():
    date = datetime.now()
    print(f"{date.strftime("%A, %B %d, %Y")}")
    choice = input("""
         [1] Write a new entry
         [2] Read past entries 
         [3] Exit 
                    """)
    while True: 
         choice = input("What would you like to do?: ").strip()
         if choice == 1:
            pass
         if choice == 2:
            pass
         if choice == 3:
            sys.exit()

main()