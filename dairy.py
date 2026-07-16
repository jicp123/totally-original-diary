#step 1: get current date for file name
#step 2: open file w date name and user input there
#step 3: command line interface
#step 4: go bullshit

from datetime import datetime
import pathlib

def main():
    date = datetime.now()
    while True:
        print(f"{date.strftime("%A, %B %d, %Y")}")
        choice = input("""
         [1] Write a new entry
         [2] Read past entries 
         [3] Exit 
                    """) 
        break
    print(choice)

main()