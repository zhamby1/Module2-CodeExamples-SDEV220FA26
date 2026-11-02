#loops are also part of the control structure category..but they repate code until a condition is met
#loops main goal is to repeat or iterate through structures until you want it stop

#while loop - a loop the repeats code until a specific condition is met, using a flag or sentinel value
#for loops - similar but they are count controlled an drepate a certain of times

#while loops are usually broken by a flag or a sentinel value.  They must be changed inside of the loop body in order to break the loop

#flag value
keep_going = "y"

#make a commission program that checks sales and commission rates.  breaks when the user is done entering values
#we use the same relational operators in loops as we do if statements
#syntax for while loop - while condition:

while keep_going == "y":
    sales = float(input("Give me your sales amount for this month "))
    com_rate = float(input("Enter your commission rate in decimal form "))

    total_earned = sales * com_rate

    print("You have earned", total_earned, "this month!")

    #flag value must be changed so we can exit loop
    keep_going = input("Do you wish to enter another months amount?  Is so press y and enter, otherwise press n and enter ")

print("Thanks for using our program")