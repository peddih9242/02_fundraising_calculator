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


def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to

# main routine

total_cost = num_check("Total cost of items? ", "Can't be 0", float)
how_many = num_check("Amount of items? ", "More than 0", int)
round_to = num_check("Round up to: ", "More than 0", int)
profit_goal = num_check("Profit Goal? ", "More than 0", float)

total_sales = total_cost + profit_goal
