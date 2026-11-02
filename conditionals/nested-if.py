#nested if statements work by having to meet multiple conditions or a series of if statements
#nested ifs mean an if statement inside of an if statement
#in this example we will voting program again to check for the us_citizen and to see if someone 18 or older

age = int(input("Please give me your age "))

if age >= 18:
    #we will have another condition besides age...us citizen needs to be true
    us_citizen = input("Are you a US citizen? Press y and enter for yes, n and enter for no ")

    if us_citizen == "y":
        print("You can vote")
    else:
        print("You cannot vote because your are not a US citizen")
else:
    print("You are too young to vote")