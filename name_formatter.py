def get_formatted_name(first_name, last_name, middle_name=""):
    """Returns full name, fully formatted"""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name.title()                                           #returns the function value

while True:                                                            #initializes the loop
    print("\nPlease tell me your name")
    print("(Enter 'q' to quit the program): ")
    f_name = input("Enter first name: ")
    if f_name == 'q':                                                  #ends the loop
        break 
    l_name = input("Enter last name: ")
    if l_name == 'q':
        break
    

    formatted_name = get_formatted_name(f_name, l_name)                #assigns the return value to the variable
    print(formatted_name)

    quit = input("\nDo you want to quit (yes/no): ")
    if quit == 'yes':
        break                                                        
    else:
        continue