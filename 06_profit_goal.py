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

        # calculate target based on profit type
        if profit_type == "%":
            target = total_costs * (profit / 100)
            return target
        else:
            return profit

total_costs = 200

for item in range(6):
    goal = get_goal(total_costs)
    # print results
    print("Profit Target: ${:.2f}".format(goal))
    print("Total Sales: ${:.2f}".format(goal + total_costs))
    print()