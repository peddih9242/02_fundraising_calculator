import pandas

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

def currency(x):
    return "${:.2f}".format(x)

# main routine

name_list = []
amount_list = []
price_list = []

# set up dictionary for components
components_dictionary = {
    "Name": name_list,
    "Amount": amount_list,
    "Price": price_list,
}

# get user data and add to list
product_name = not_blank("Product name: ", "Please enter your product name!")

what_component = ""
while what_component.lower() != "xxx":

    what_component = not_blank("What component? ", "Please enter your components!")

    if what_component.lower() == "xxx":
        break

    name_list.append(what_component)

    component_cost = num_check("Cost of component? ", "Please enter a number above 0.", float)
    price_list.append(component_cost)

    component_amount = num_check("Amount of component? ", "Please enter an integer above 0.", int)
    amount_list.append(component_amount)
    print()

# set up printing
component_frame = pandas.DataFrame(components_dictionary)
component_frame = component_frame.set_index("Name")


component_frame['Total'] = \
    component_frame["Amount"] * component_frame["Price"]

component_sub = component_frame['Total'].sum()

dollar_format = ["Price", "Total"]
for item in dollar_format:
    component_frame[item] = component_frame[item].apply(currency)

print()
print(component_frame)
print()
print("Variable Costs: ${:.2f}".format(component_sub))