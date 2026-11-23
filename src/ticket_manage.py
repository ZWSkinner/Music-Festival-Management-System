"""
The main structure for ticket management
of the music festival management system
"""

tickets_remaining = 0

ticket_name = ""
ticket_price = ""
ticket_quantity = ""

ticket_record = []
current_ticket = []

#Program introduction
print("#################################")
print("Welcome to the ticket management interface")
print("#################################")




def create_ticket():
    ticket_name = input("Ticket name: ")
    ticket_price = int(input("ticket price: "))
    ticket_quantity = int(input("ticket quantity: "))

def read_ticket():
    for i in range(len(ticket_record)):
        print(ticket_record[i])

def update_ticket(ticket_name):
    for i in range(len(ticket_record)):
        if ticket_name == ticket_record[i][1]:
            print(f"The current ticket info is: {ticket_record[i]}")

    update_operation = input("Do you wish to change [N]ame, [P]rice, or [Q]uantity?: ").lower()
    if update_operation == "N" | update_operation == "name":
        print("What do you want the new name to be?: ")  
    #provide rest of functionality

"""
def delete_ticket():



def buy_ticket():


"""
#Loops infinitely until exit is entered
# !!! Still need to incorporate exit in every input unless crtl+c
while (ticket_operation != "exit"):

    ticket_operation = input("what do you wish to do?:\n[C]reate\n[R]ead\n[U]pdate\n[D]elete\n[B]uy").lower()

    if (ticket_operation == "c") | (ticket_operation == "create"):
        create_ticket()

    elif (ticket_operation == "r") | (ticket_operation == "read"):
        read_ticket()

    elif (ticket_operation == "u") | (ticket_operation == "update"):
        ticket_name = input("what is the name of the record to delete?: ")
        update_ticket(ticket_name)

    elif(ticket_operation == "d") | (ticket_operation == "delete"):
        delete_ticket()

    elif(ticket_operation == "b") | (ticket_operation == "buy"):
        buy_ticket()

    elif(ticket_operation == "exit"):
        break

    else:
        print("That is not a valid operation.")