profit_goal = input("Profit goal? ")

if profit_goal [0] == "$":
    profit = profit_goal[1:]
elif profit_goal [-1] == "%":
    profit = profit_goal[:-1]
else:
    if profit_goal <= 100:
        profit = input("Did you mean {}%".format(profit_goal))