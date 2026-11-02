#if statements in python are single alternative and allow you to create branches is code
#conditional statements allow us to create these alternate paths or branches
#they rely realtional operators - <,>,<=,>=,==,!=

#lets look to create an if statement to see if two values are equal
#if statements do not have to use the () and {} like other languages
#instead we use indentation to denote blocks of code
#syntax is if condition:  followed by indented block of code

#if true code runs if not line skipped
a = 5
b = 5

#dont forget that == compares values and = assigns values
if a == b:
    #indentation does matter in python and it is how we determine blocks of code
    print("These are equal")

#greater than equal to
c = 6
d = 7

if d >= c:
    print("D is greater than or equal to C")


#we can also use strings
us_citizen = "y"

if us_citizen == "y":
    print("You can vote")


#when evaluating values, you get a true or false back and we can actually use True and False as boolean values in Python
mybool_true = True
mybool_false = False

#not equal - not in python can be used as a compound or relation operator

x = 45
y = 88

if x != y:
    print("X and Y are not equal")