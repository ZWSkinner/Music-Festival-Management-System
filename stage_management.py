import csv
from pathlib import Path

STAGES_FILE = Path(__file__).with_name("stages.csv")

def stage_management():
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
        stage_management()

def add():
    stname = input("provide stage name: ")
    stcap = int(input("provide stage capacity: "))
    stloc = input("provide stage location: ")
    print(f"Stage name: {stname}, Stage capacity: {stcap}, Stage location: {stloc}")
    data = [
    ["Stage Name", "Stage Capacity", "Stage Location"],
    [stname, stcap, stloc]
    ]
    with open(STAGES_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    stage_management()

def view():
    stage_to_view = input("what stage do you want to view? ")
    with open(STAGES_FILE, newline="", encoding="utf-8") as f:
        for stage in csv.DictReader(f):
            if stage["Stage Name"].casefold() == stage_to_view.strip().casefold():
                print(
                    f"Stage Name: {stage['Stage Name']}, "
                    f"Stage Capacity: {stage['Stage Capacity']}, "
                    f"Stage Location: {stage['Stage Location']}"
                )
                return

    print(f"Stage not found: {stage_to_view}")

if __name__ == "__main__":
    stage_management()