#step 1: get current date for file name
#step 2: open file w date name and user input there
#step 3: command line interface
#step 4: go bullshit

from datetime import datetime
import pathlib
import sys
import re
def main():
    date = datetime.now()
    print(f"{date.strftime("%A, %B %d, %Y")}")
    print(f"{date.strftime("%Y-%m-%d %H:%M:%S")}")
    print("""
         [1] Write a new entry
         [2] Read past entries 
         [3] Exit 
                    """)
    while True: 
         choice = input("What would you like to do?: ")
         if choice == "1":
            writenew(date)
            break
         elif choice == "2":
            pass
         elif choice == "3":
            sys.exit()
         else:
             print("Invalid input.")

def writenew(date):
    filename = date.strftime("%m-%d, %Hh%Mm%Ss")
    filepath = pathlib.Path("log")/filename
    with open(filepath, "a") as file:
        entry = input("Start writing here: ")
        file.write(f"{entry}")  

def view():
    filenames = {}
    path = pathlib.Path("log")
    for i, x in enumerate(path.iterdir(), 1):
        filenames[i] = x.stem 
    print(filenames)

    while True:
     choose = input("Which would you like to view? (Input the number): ").strip()
   
     filenames[choose] 
     #except KeyError:
        #print("Input a valid number.")
        #print(filenames)
    


view()