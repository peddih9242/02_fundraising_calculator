def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main routine
for item in range(4):
    float_number = num_check("Float money amount: $", "Please enter a number above 0.", float)
for item in range(4):
    integer_number = num_check("Integer money amount: $", "Please enter an integer (whole number) above 0.", int)
