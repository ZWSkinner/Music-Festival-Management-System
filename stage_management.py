def stage_management():
    stageinput = input("What do you want? add/view/update/delete: ").lower()
    print(stageinput)
    if stageinput == "add":
        add()

    elif stageinput == "view":
        view()

    elif stageinput == "update":
        update()

    elif stageinput == "delete":
        delete()
        
    else:
        print("Please try again. You can only add, view, update or delete.")
        stage_management()

def add():
    stname = input("provide stage name: ")
    stcap = int(input("provide stage capacity: "))
    stloc = input("provide stage location: ")
    print(f"Stage name: {stname}, Stage capacity: {stcap}, Stage location: {stloc}")

def view():
    
    stage_to_view = input("what stage do you want to view? ")
    print(f"Viewing stage: {stage_to_view}")

if __name__ == "__main__":
    stage_management()