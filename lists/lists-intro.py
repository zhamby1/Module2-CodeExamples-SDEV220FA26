#data structures - define how data is stored and organized outside of normal data types (int,float,string)
#what a list unique is that we can store multiple pieces of information or data that is located under one name
#python's simpliest data structure - list
#this is similar to an array but with a few differences

#lists are dynamic in size - no set size and can increase and decrease when needed
#lists can also contain multiple data types (often times you dont want to do this)
#lists are mutable - they can be changed after created
#aka items can be modified, deleted, or inserted

#to create a list the syntax is - nameoflist = []
#a list can be initialized with data or it can be empty
#if you initalize a list with data, make sure you use a , between each data item
names = []
test_scores = [100,95,82,85,40,77]

#to modify or grab data from a list, we have to know its index or use a function to grab and find it
#an index is the location within the list that points to the data value
#we have to use an index because each individual value does not a variable name
#the index at python starts out at 0, in the above example that means if we print test_scores[0] we would see 100 on the screen
print(test_scores[0])
print(test_scores[2])

#we can also add data to a list using the append() function
#we can say nameoflist.append(data)

names.append("Zach")
names.append("Aly")
names.append("Shirley")

#you can also do a debug print of the list if you say print(listname)
#this isn't to be used to display to the user but as a form of debugging and testing
print(names)

#one of the biggest advantages of using a list is the ability to loop, search and process data in a list
#for instance, if we need to dispaly all the data in a list, we could doe the horrible task of tryin to print each item one line at a time
#instead we can use a loop to grab all the data

#for in loop - count the number of items IN a list for us, and loop through it
#syntax  - for variable_name_that_represents_a_single_item in list_name

#the variable name represents each individual item in the list
for score in test_scores:
    print(score)

#python also has some built in features to look for things without having to loop...looping will depend on your situation
#search feature of a list where we can just use the in keyword to see if a value is in a list and it will search for us
#it will return a true or false
looking_for = "Zach"
found = looking_for in names
print(found)

#.index() function/method that can return an index of a value if it is found
#this could crash we are going to look a safer way
index_modify = names.index("Aly")
names[index_modify] = "Alyson"
print(names)

looking_for = "Alyson"

if looking_for in names:
    print(names.index(looking_for))
else:
    print("Not found")
