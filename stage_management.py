import csv
from pathlib import Path
"""todo:
add functionality to update and delete stages.
add persistence to the stages dictionary using a file type try json.
after all done change back #inputs as its easier to make pytests without inputs.
"""
stages = {}

def stage_management(stageinput):
    while True:
        stageinput = stageinput.lower()
        #input("What do you want? add/view/update/delete/exit: ")
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
            return ("Exiting the stage management system.")

        else:
            return ("Please try again. You can only add, view, update or delete.")

def add(stname,stcap,stloc):
    stname =  stname
    #input("provide stage name: ")
    while True:
        try:
            stcap = int(stcap)
            #input("provide stage capacity: ")
            break
        except ValueError:
            return ("Invalid input. Please enter a valid number for stage capacity.")
    stloc =  stloc
    #input("provide stage location: ")
    stages[stname] = {
        "Stage Name": stname,
        "Stage Capacity": stcap,
        "Stage Location": stloc,
    }
    result = "added stage successfully"
    return result

def view(stage_to_view):
    stage_to_view = stage_to_view
    #input("provide stage name to view: ")
    if stage_to_view == "All":
        result = ""
        for stage_name, stage_data in stages.items():
            result += (
                f"Stage Name: {stage_data['Stage Name']}, "
                f"Stage Capacity: {stage_data['Stage Capacity']}, "
                f"Stage Location: {stage_data['Stage Location']}\n"
            )
        return result

    if stage_to_view in stages:
        data = stages[stage_to_view]
        result = (
            f"Stage Name: {data['Stage Name']}, "
            f"Stage Capacity: {data['Stage Capacity']}, "
            f"Stage Location: {data['Stage Location']}"
        )
        return result


    return f"Stage not found: {stage_to_view} Please try agian."

def update():
    return

def delete():
    return

if __name__ == "__main__":
    stage_management()