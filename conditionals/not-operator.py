#not by itself doesnt really work without another comparison
#not flips a true to a false or a false to a true

x = 15

#nots are often used with other compound operators to get a result

#for instance, I want to see if X DOES NOT equal 10 or 11
#to use a not we say not() and inside the () we put the condition to be evaluated and flipped

if not(x == 10 or x == 11):
    print("X is not equal to 10 or 11")

else:
    print("x is equal to either 10 or 11")