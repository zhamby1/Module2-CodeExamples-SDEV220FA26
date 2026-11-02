#or means only ONE of the conditions must be true for the block of code to run
#lets use an example of discounted movie tickets

#tickets at a theatre get a discount oftentimes based on how old your are
#in our example, children 12 and under get a child discount and senior citizens 65 and older get the sc discount

ticket_price = 10.00
discount = 0.10

age = int(input("How old are you? "))

#make sure even though we will be using one variable to make comparisions, that you use that variable name on both sides of the or statement
#you cannot say if age <= 12 or >= 65....you need something to always compare
#the or operator is just the word or

if age <= 12 or age >= 65:
    ticket_price = ticket_price - (ticket_price * discount)
    print("You get a discount.  Your ticket price is", ticket_price)

else:
    print("Your ticket price", ticket_price)