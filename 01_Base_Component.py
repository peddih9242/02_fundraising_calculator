import pandas
import math

# Functions

# number checking function, checks for number above 0 and
# sets number type
def num_check(question, error, num_type):
    
    # start loop
    valid = False
    while not valid:
        try:

            # ask for input
            response = num_type(input(question))
            
            # check number is above 0
            if response <= 0:
                print(error)
            else:
                return response

        # if input is not a number, print error
        except ValueError:
            print(error)

# string checking function, refers to given list for valid input
def string_checker(question, error, valid_list):
    
    # start loop
    valid = False
    while not valid:
        
        # ask user for input
        response = input(question).lower()
        
        # check everything in list for first letter or full word
        for var_item in valid_list:
            if response == var_item or response == var_item[0]:
                return var_item
        
        # if nothing found as valid, print error
        print(error)

# function for getting variable / fixed costs and setting up printing
def get_costs(var_fixed):

    # set up lists and dictionary
    count = 0
    var_name = []
    var_amount = []
    var_price = []

    variable_cost_dict = {
        "Name": var_name,
        "Amount": var_amount,
        "Price": var_price
    }

    # get user data and add to list

    loop_cost = ""
    while loop_cost == "":

        what_component = not_blank("What component? ", "Please enter your components!")

        if what_component.lower() == "xxx":
            if count == 0:
                print("Please enter a component first!")
                continue
            else:
                break

        var_name.append(what_component)

        component_cost = num_check("Cost of component? $", "Please enter a number above 0.", float)
        var_price.append(component_cost)
        if var_fixed == "variable":
            component_amount = num_check("Amount of component? ", "Please enter an integer above 0.", int)
        else:
            component_amount = 1    
        count += 1
        var_amount.append(component_amount)
        print()

    # set up printing
    component_frame = pandas.DataFrame(variable_cost_dict)
    component_frame = component_frame.set_index("Name")

    component_frame['Total'] = \
        component_frame["Amount"] * component_frame["Price"]

    component_sub = component_frame['Total'].sum()

    dollar_format = ["Price", "Total"]
    for item in dollar_format:
        component_frame[item] = component_frame[item].apply(currency)

    return [component_frame, component_sub]

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

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# function for printing variable / fixed frame and subtotal
def cost_printing(heading, frame, subtotal):
    print()
    print("*** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

# get the profit goal
def get_goal(total_costs):
    
    error = "Please enter a dollar amount or percentage."
    
    # start loop
    valid = False
    while not valid:

        # get response
        wanted_profit = input("Profit goal? ")

        # check for $ or % sign, split string into profit type and amount
        if wanted_profit[0] == "$":
            profit_type = "$"
            profit = int(wanted_profit[1:])

        elif wanted_profit[-1] == "%":
            profit_type = "%"
            profit = int(wanted_profit[:-1])

        else:
            profit_type = "unknown"
            profit = wanted_profit

        # check that number is valid
        try:
            profit = float(profit)
            if profit <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        # if only given a number, ask what they meant based on number
        if profit <= 100 and profit_type == "unknown":
            check_type = string_checker("Did you mean {}%? ".format(profit), "Please enter yes or no.", yes_no)
            if check_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        elif profit > 100 and profit_type == "unknown":
            check_type = string_checker("Did you mean ${}? ".format(profit), "Please enter yes or no.", yes_no)
            if check_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        # calculate target based on profit type
        if profit_type == "%":
            target = total_costs * (profit / 100)
            return target
        else:
            return profit

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# main routine

yes_no = ["yes", "no"]

# get product name
product_name = not_blank("Product name: ", "Please enter your product name!")
how_many = num_check("How many items will you be producing? ", "Please enter an integer above 0.", int)

print()

# get variable costs
print("**** Variable Costs ****")
variable_costs = get_costs("variable")
variable_frame = variable_costs[0]
variable_sub = variable_costs[1]
print()

have_fixed = string_checker("Do you have fixed costs? ", "Please enter yes / no.", yes_no)

if have_fixed == "yes":
    print()
    # get fixed costs
    print("**** Fixed Costs ****")
    fixed_costs = get_costs("fixed")
    fixed_frame = fixed_costs[0]
    fixed_sub = fixed_costs[1]
else:
    fixed_sub = 0

# get recommended price
total_costs = variable_sub + fixed_sub

profit_goal = get_goal(total_costs)

sales_needed = total_costs + profit_goal

round_to = num_check("Round to nearest? ", "Please enter an integer above 0.", int)

selling_price = sales_needed / how_many
recommended_price = round_up(selling_price, round_to)

print()
print("**** Fund Raising - {} ****".format(product_name))
print()
cost_printing("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    cost_printing("Fixed", fixed_frame[["Total"]], fixed_sub)

print()
print("Total Costs: ${:.2f}".format(total_costs))
print()

print("Profit Target: ${:.2f}".format(profit_goal))
print("Total Sales: ${:.2f}".format(profit_goal + total_costs))

print()

print("**** Pricing ****")
print("Minimum Price: ${:.2f}".format(selling_price))
print("Recommended Price: ${:.2f}".format(recommended_price))

# change dataframe to string (so that it can be written into a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)

# write to file
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
text_file.write("**** Fund Raising - {} ****".format(product_name))
text_file.write(variable_txt)