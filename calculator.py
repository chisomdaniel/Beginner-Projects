# The aim here is to write a code that collect two numbers from the user and tell the greater number between the both
# Also, the code keeps repeating as long as the user wants to

def calculator(a, b):
    if a > b:
        print("yes " + str(a) + " is greater than " + str(b))
        print(" ")
    else:
        print("no " + str(b) + " is greater than " + str(a))
        print(" ")


time = ""


def repeat(time2):
    while time2 != "no":
        calculator(a=int(input("type the first number: ")), b=int(input("type another number: ")))
        time2 = input("Do you want to continue(Enter 'no' to stop): ")
        time2 = time2.lower()


repeat(time2=time)

# Honestly I'm a little confused why this code works 'cus "time" is the parameter passed to the function, and as far as this code is, time is an empty string.
# Incase you eventually find out, would appreciate if you let me know ;)
