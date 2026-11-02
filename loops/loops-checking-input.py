#lets say you need to check some data types for your program
#in other words I need to see if a user enters a number instead of text
#we can use loops and the built in functions/methods for variables to help us with this

while True:
    #grab age but do not convert it yet.  we want to make sure age is a number
    age = input("Please enter your age as a numerical value ")

    #there are all sorts of built in functions/methods for our values and data types.  one is called isdigit() and will check if a value is a number
    if age.isdigit():
        age_converted = int(age)
        print("Your age is", age_converted)
        break
    else:
        print("Invalid input please enter a numerical value")