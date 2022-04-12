import math

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
            check_type = input("Did you mean {}%? ".format(profit))
            if check_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        elif profit > 100 and profit_type == "unknown":
            check_type = input("Did you mean ${}? ".format(profit))
            if check_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        # calculate profit target based on profit type
        if profit_type == "%":
            target = total_costs * (profit / 100)
            return target
        else:
            return profit

def round_up(amount, var_round_to):
    try:
        amount = int(amount)
        return float(math.ceil(amount / var_round_to)) * var_round_to + var_round_to
    except ValueError:
        return float(math.ceil(amount / var_round_to)) * var_round_to

# main routine

# get needed input and print stats
total_cost = num_check("Total cost of items? ", "Can't be 0", float)
how_many = num_check("Amount of items? ", "More than 0", int)
round_to = num_check("Round up to: ", "More than 0", int)
profit_goal = get_goal(total_cost)

sales_needed = total_cost + profit_goal

print("Total: ${:.2f}".format(total_cost))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))