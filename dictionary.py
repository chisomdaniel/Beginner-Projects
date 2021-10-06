# Aim: To Create a dictionary with info of all family members in another dictionary
# Read through, you understand ;)
# Feel free to make your own clone of this project and add any cool update of feature you like ;)

Family = {}


def create_dic(first_name, last_name, user_name, class1="NIL", level="NIL", **other_info):
    # add values to a dictionary and put a default value for any unavailabe input, there is also spaces for unkmown input
    dictionary = {
        "first name": first_name,
        "last name": last_name,
        "user name": user_name,
        "class": class1,
        "level": level,
    }
    for keys, values in other_info.items():  # add the unknown value to the dictionary
        dictionary[keys] = values
    Family[first_name] = dictionary  # pick the dictionary from the main code and append the new dictionary to it
    return Family


begining = input("do you want to add any family member today? Yes or No: ")
begining = begining.lower()

if begining == "yes":
    Family = create_dic(first_name=input("what is your first name?(COMPULSORY): "), last_name=input("what is your last name?(COMPULSORY): "), user_name=input("Enter a username(COMPULSORY): "), class1=input("enter class(opt): "), level=input("enter level(opt): "), school=input("enter school(opt): "), college=input("enter college(opt): "), weight=input("Enter weight: "))  # calling the function
    question = input("do you want to print the dictionary? Yes or No: ")
    question = question.lower()
    if question == "yes":
        print(Family)
    else:
        print("Ok then, you are good to go")
    ask = input("Do you want to add more members?(Yes or No): ")
    ask = ask.lower()
    while ask == "yes":  # forever loop to add more members until the person input "no"
        Family = create_dic(first_name=input("what is your first name?(COMPULSORY): "), last_name=input("what is your last name?(COMPULSORY): "), user_name=input("Enter a username(COMPULSORY): "), class1=input("enter class(opt): "), level=input("enter level(opt): "), school=input("enter school(opt): "), college=input("enter college(opt): "), weight=input("Enter weight: "))
        question = input("do you want to print the dictionary? Yes or No: ")
        question = question.lower()
        if question == "yes":  # determine weather to print the dictionary or not
            print(Family)
        else:
            print("Ok then, you are good to go")
        ask = input("do you want to add again?(Yes or No): ")
else:
    print("Ok then, goodbye :)")
