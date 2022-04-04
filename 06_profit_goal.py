

def profit_goal(total_costs):
    profit_type = 0
    valid = False
    while not valid:
        try:
            profit_goal = input("Profit goal? ")

            # check for $ or % sign, split string into profit type and amount
            if profit_goal[0] == "$":
                profit_type = "$"
                profit = int(profit_goal[1:])

            elif profit_goal[-1] == "%":
                profit_type = "%"
                profit = int(profit_goal[:-1])

            else:
                
                profit_goal = int(profit_goal)
                # if only given a number, ask what they meant based on number
                if profit_goal <= 100:
                    profit = input("Did you mean {}%".format(profit_goal))
                    if profit_goal == "yes":
                        profit_type = "%"

                elif profit_goal > 100:
                    profit = input("Did you mean ${}".format(profit_goal))
                    profit_goal = "$"
                else:
                    print("Please enter a dollar amount or percentage.")
                    continue
        
        except ValueError:
            print("Please enter a dollar amount or percentage.")

        # calculate target based on profit type
        if profit_type == "%":
            profit /= 100
            target = total_costs * profit
        else:
            target = profit
        return target

total_costs = 200

goal = profit_goal(total_costs)
# print results
print("Profit Target: ${:.2f}".format(goal))
print("Total Sales: ${:.2f}".format(goal + total_costs))