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

# main routine

yes_no = ["yes", "no"]

for item in range(0,3):
    string_test = string_checker("Yes or no? ", "Please enter yes / no.", yes_no)
    print("You chose", string_test)