# defining a function for making a list of the elements seperated by the hyphen 

def alpha():
    user_input = input('Enter words seperated by hyphen: ')
    # The function is arragend alphabetically

    input_list = sorted(user_input.split('-'))
    # The function is then joined 
    
    print('-'.join(input_list))


# Calling the function
alpha()


    
    

