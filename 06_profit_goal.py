def get_goal(total_costs):
    error = "Please enter a dollar amount or percentage."
    profit_type = 0
    valid = False
    while not valid:
        # get response
        profit_goal = input("Profit goal? ")

        # check for $ or % sign, split string into profit type and amount
        if profit_goal[0] == "$":
            profit_type = "$"
            profit = int(profit_goal[1:])

        elif profit_goal[-1] == "%":
            profit_type = "%"
            profit = int(profit_goal[:-1])

        else:
            profit_type = "unknown"
            profit = profit_goal

        # check that number is valid
        try:
            profit_goal = float(profit_goal)
            if profit_goal <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        # if only given a number, ask what they meant based on number
        if profit_goal <= 100 and profit_type == "unknown":
            profit = input("Did you mean {}%? ".format(profit_goal))
            if profit == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        elif profit_goal > 100 and profit_type == "unknown":
            profit = input("Did you mean ${}? ".format(profit_goal))
            if profit == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        # calculate target based on profit type
        if profit_type == "%":
            target = total_costs * (profit_goal / 100)
            return target
        else:
            return profit_goal

total_costs = 200

for item in range(6):
    goal = get_goal(total_costs)
    # print results
    print("Profit Target: ${:.2f}".format(goal))
    print("Total Sales: ${:.2f}".format(goal + total_costs))