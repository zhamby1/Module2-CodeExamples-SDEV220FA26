#if else statements are dual alternative - two branching paths
#else is a catch-all for any situation that the if statement does not evaluate to True

#example using strings - if/else accpet terms and conditions
terms_and_conditions = input("Do you accept the terms and conditions? Type in yes and enter for yes, no and enter for no ")

if terms_and_conditions == "yes":
    print("Thank you for accepting the terms and conditions")
else:
    print("Access denied..you did not accept the T&C")


#checking to see if your are old enough to vote (18 and older)
#make sure that if using input you are using the right data type or value
age = int(input("Please give me your age "))

if age >= 18:
    print("You can vote")

else:
    print("You CANNOT vote")