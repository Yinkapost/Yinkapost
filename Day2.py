# Day 2 - Type Error, Checking and Conversion
# you cant concatenate two different types of data types. so you will need to convert one to the other before your program can run.
num_char = len(input("What is your name?\n"))
new_num = str(num_char)
# if we print a message with strings without converting the input result(an integer) to a string, it will return an error
# print(f"Your name has " {num_char} " characters!") will print an error
print(f"Your name has {new_num} characters!")
# You can use the typefunction to chek the type of data
print(type(num_char))
print(type(new_num))
#Int and float work together but they dont work with strings. So you need to convert
print(70 + float("100.5"))
print(str(70) + str("100.5"))

#assignment1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
twoo = int(two_digit_number[1]) + int(two_digit_number[0])
print(twoo)

#assignment 2: Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. 
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m). Result must be a wholenumber
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height))
# new_height = float(height) * float(height)
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))

# No manipulation and F-string
# round function casn be used to round a decimalnumber into the nearest whole number as opposed chopping off all numbers after the decimalwhichhapopens with the int()
print("round----------------------")
print(round(8 / 3))
# can also specify the number of digits you want to round it to
print(round(8 / 3, 2))
print("int with //-----------------------")
print(8 // 3)
# continue performing actions on a variables using the +=, -=, *=, or /=
print("continue variables ---------------------")
score = 1
#user scores 2 more points
score += 2
print(score)
# Using the f-String- allows you to add different type of data types in a string without having to convert all to strings 
print("F-string-----------") 
score = 2 #int
height = 1.75 #float
isWinning = True #booleon
print(f"Your score is {score}; your height is {height}; and your are winning is {isWinning}")
# assignment 3: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
print("assignment3------")
      # 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆
# #Write your code below this line 👇
day90 = 90 * 365
week90 = 90 * 52
month90 = 90 * 12

used_day = int(age) * 365
used_week = int(age) * 52
used_month = int(age) * 12

rem_day = day90 - used_day
rem_week = week90 - used_week
rem_month = month90 - used_month

message = f"You have {rem_day} days, {rem_week} weeks, and {rem_month} months left. "

print(message)

# as treated by abgela
# age = input("What is your current age? ")

# years = 90 - int(age)
#months = round(years * 12)
#weeks = round(years * 52)
#days = round(years * 365)

#print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# final Day 2 project - create a tip calculator that calculates howmuch each person pays + tip
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill?")
tip = input("How much tip would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill?")

tip_per = (float(tip)/100 * float(bill)) / float(split)
print(tip_per)

float_bill = float(bill)
print(float_bill)
float_split = float(split)
print(float_split)

per_person = (float_bill / float_split) + tip_per
print(per_person)
rounded_per_person = (round(per_person, 2))
print(f"Each person's bill with tip is ${rounded_per_person}")

# angela solution
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")














