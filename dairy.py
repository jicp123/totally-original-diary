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
    print(f"{date.strftime("%Y-%m-%d %H:%M:%S")}")
    choice = input("""
         [1] Write a new entry
         [2] Read past entries 
         [3] Exit 
                    """)
    while True: 
         choice = input("What would you like to do?: ").strip()
         if choice == 1:
            writenew(date)
         if choice == 2:
            pass
         if choice == 3:
            sys.exit()

def writenew(date):
    filename = date.strftime("%m-%d %H:%M")
    filepath = pathlib.Path("log")/filename
    with open(f"{filepath}", "a") as file:
        entry = input("Start writing here: ")
        file.write(f"{entry}")

main()