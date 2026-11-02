#compound conditions and their operators allow for multiple conditions inline with our if statement
#there are three types of compound operators

# and - both conditions must be true for the block of code to run
# or - only ONE condition must be true for the block of code to run
# not - flips boolean result to it's opposite

#truth tables to get the result

#and compound operator - lets take the voting program and using the and operator instead of nesting

age = int(input("Please enter your age "))
us_citizen = input("Are you a US citizen?  If so, press y and enter for yes, n and enter for no ")

#to use the and operator just type in the word
#other languages use the &&, but python just uses the word and

if age >=18 and us_citizen == "y":
    print("You can vote")

else:
    print("You cannot vote")