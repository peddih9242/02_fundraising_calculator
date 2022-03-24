# functions

# number checker
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# check for blank
def not_blank(question, error):
    loop = True
    while loop is not False:
        response = input(question)
        if response == "":
            print(error)
            print()
        else:
            return response


# main routine

name = []
amount = []
price = []


components_dictionary = {
    "Name": name,
    "Amount": amount,
    "Price": price,
}

how_many = num_check("How many items are you making? ", "Please enter an integer above 0.", int)

what_item = input("What item are you making? ")

while what_component != "xxx":
    what_component = input("What component? ")
    component_cost = num_check("Cost of component? ", "Please enter a number above 0.", float)
    component_amount = num_check("Amount of component? ", "Please enter an integer above 0.", int)
