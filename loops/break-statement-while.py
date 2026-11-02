#sometimes we want use a loop to check for certain conditions in order to program defensivly
#what I mean by that is not continuing a program until a condition is met
#we can use a flag within a while to do that, but there can be alternatives

#There is another way in python we can explicity tell the loop to break or continue until you encounter the break keyword
#the break keyword allows us to break a loop anytime it is used

#this is great because we dont necessarily have to create a loop variable
#instead we can say while True and then use the break keyword to break the loop

#you must accept the terms and conditions before moving on

while True:
    accept = input("Do you accept the terms and conditions? Press y and enter for yes ")

    #we can use a condition to break out of the loop using break
    if accept == "y":
        print("Access Granted")
        break
    else:
        print("You cannot get access until you accept the T&C")


print("Welcome to Zach's Program")