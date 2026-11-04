#for loops are loops that repeat code a certain number of times ie count controlled
#python is a little different when it comes to for loops..there are many ways to do this in other languages but they usually fall into this format

# for(int i = 0; i < 11; i++)
# where I represents the iterator/counter variable, the second argument represents the condition, and their argument represent the step or increment

# what python does differently is it uses a for in loop with a function called range() to iterate over a range of values
#for in loop - uses the in keyword to tell a variable what to loop through (more into that when we talk about lists)
#however we can use a for in loop just to loop over ranges

#syntax in a for in loop - for i in range(start,stop,increment/step)
number = 6
for i in range(0,number,1):
    print(i)

print("*********************")

#we can also short hand the for in range loop if we know we are starting at 0 and counting up by 1
for i in range(number):
    print(i)

print("***********************")

#we can also count down using negative steps (using negative decrements instead aka negative numbers)
for i in range(10,0,-1):
    print(i)

print("*******************")

#we can set our increment/step by other values than 1
for i in range(0,40,2):
    print(i)