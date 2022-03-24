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