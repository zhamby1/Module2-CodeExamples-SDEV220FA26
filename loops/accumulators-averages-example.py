#we can use loops as accumulators (running totals)
#this program is a program that averages numbers
# average - total / how_many_number

sum = 0 
average = 0

#we can have users control loop values by asking for input..if so make sure that it is always a whole number when using a for loop
how_many_numbers = int(input("Please enter how many numbers you wish to average "))

#we can use either loop for this, but I will use a for loop
for i in range(how_many_numbers):
    #create a input variable that will ask for a value each time the loop is ran
    number = float(input("Please enter a number you wish to average "))

    #accumulator - keeps up with our running total
    sum = sum + number 

print("Your total sum is", sum)

#our average can work by taking the sum total and dividing it by our how_many_numbers counter
average = sum / how_many_numbers

print("Your average is", average)