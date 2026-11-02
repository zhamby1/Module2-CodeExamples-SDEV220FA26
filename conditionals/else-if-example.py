#else-if statements are multi alternative that can have more than one branching path
#usually deals with ranges or having multiple choice or conditions type of evaluation

#python does not have a switch-case structure...so anything you would use for switch-case you have to else-if
#below is a program that we will convert a numerical grade to a letter grade

#ie A = 90-100  B = 80-89   C = 70-79   D = 60-69  F <= 59

number_grade = 82
letter_grade = ""

if number_grade >= 90:
    letter_grade = "A"

#else-if statements use the elif keyword
#short circuit evaluation - the code exits upon meeting a condition and skips the rest of the elif structure
#in this case if my number grade is 85 the first condition it meets is the one below, thus skipping the rest
#2 advantages - saves processing power
#another is that we can sometimes ignore ranges and giving upper limits

elif number_grade >= 80:
    letter_grade = "B"

elif number_grade >= 70:
    letter_grade = "C"

elif number_grade >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"


print("Your letter grade is", letter_grade)