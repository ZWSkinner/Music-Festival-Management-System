import csv
from pathlib import Path
"""TODO:
add functionality to update and delete stages.
add persistence to the stages dictionary using a file type try json.

"""
stages = {}

def stage_management():
    while True:
        stageinput = input("What do you want? add/view/update/delete/exit: ").lower()
        print(stageinput)
        if stageinput == "add":
            add()

        elif stageinput == "view":
            view()

        elif stageinput == "update":
            update()

        elif stageinput == "delete":
            delete()

        elif stageinput == "exit":
            print("Exiting the stage management system.")
            return

        else:
            print("Please try again. You can only add, view, update or delete.")

def add():
    stname = input("provide stage name: ")
    while True:
        try:
            stcap = int(input("provide stage capacity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for stage capacity.")
    stloc = input("provide stage location: ")
    stages[stname] = {
        "Stage Name": stname,
        "Stage Capacity": stcap,
        "Stage Location": stloc,
    }
    print(f"Stage Name: {stname}, Stage Capacity: {stcap}, Stage Location: {stloc}")

def view():
    stage_to_view = input("what stage do you want to view? ")
    if stage_to_view in stages:
        data = stages[stage_to_view]
        print(
            f"Stage Name: {data['Stage Name']}, "
            f"Stage Capacity: {data['Stage Capacity']}, "
            f"Stage Location: {data['Stage Location']}"
        )
        return


    print(f"Stage not found: {stage_to_view}")

def update():
    return

def delete():
    return

if __name__ == "__main__":
    stage_management()