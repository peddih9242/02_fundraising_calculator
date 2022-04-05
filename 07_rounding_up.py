import math

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to
# main routine
round_test = [2.75, 2.25, 2]

for item in round_test:
    rounded = round_up(item, 1)
    print("${:.2f} --> ${:.2f}".format(item, rounded))