# Control flow and logical operators
#Assignment1: Write a program that works out whether if a given number is an odd or even number. 
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# nested if/elif/else - elif can be infinite
age = int(input("How old are you?\n"))
height = int(input("How tall are you?\n"))

if height >= 180:
    if age < 5:
        print("Your ticket price is $6")
    elif age <= 18:
        print("Your ticket price is $21")
    else:
        print("Your price is $50")
else:
    print("Sorry, you cant ride.")

#Assignment 2: Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2)
rounded_bmi = round(BMI)

if rounded_bmi <= 35:
  if rounded_bmi < 18:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
  elif rounded_bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
  elif rounded_bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
  elif rounded_bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
  print(f"Your BMI is {rounded_bmi}, you are clinically obese.")
# Write a program that works out whether if a given year is a leap year.
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year.")
    else:
      print("Not Leap Year.")
  else:
    print("Leap Year.")  
else:
  print("Not Leap Year.")
  
# EXTENSION OF THE NESTED IF EQUATION
age = int(input("How old are you?\n"))
height = int(input("How tall are you?\n"))

bill = 0
if height >= 180:
    if age < 5:
        bill =+ 6
        print(f"Your ticket price is ${bill}")
    elif age <= 18:
        bill =+ 21
        print(f"Your ticket price is ${bill}")
    else:
        bill =+ 50
        print(f"Your ticket price is ${bill}")
        
    photos = input("Want photos? Y or N")
    if photos == "Y":
        bill =+ 3
        print(f"Your new bill is ${bill}")
    else:
        print(f"Your ticket price is ${bill}")
else:
    print("Sorry, you cant ride.")
    

# EXTENSION OF THE NESTED IF EQUATION
age = int(input("How old are you?\n"))
height = int(input("How tall are you?\n"))
bill = 0
if height >= 180:
    if age < 5:
        bill = 6
        print(f"Your ticket price is $6")
    elif age <= 18:
        bill = 21
        print(f"Your ticket price is $21")
    else:
        bill = 50
        print(f"Your ticket price is $50")
        
    photos = input("Want photos? Y or N\n")
    if photos == "Y":
        bill += 3
    print(f"Your new bill is ${bill}")     
else:
    print("Sorry, you cant ride.")

# Pizza ass - build an automatic pizza order program.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price = 0
if size == "S":
  price += 15
  if add_pepperoni == "Y":
    price += 2
  if extra_cheese == "Y":
    price += 1
    print(f"Your bill for Small Pizza is ${price}")
  else:
    print(f"Your bill for Small Pizza is ${price}")
elif size == "M":
  price += 20
  if add_pepperoni == "Y":
    price += 3
  if extra_cheese == "Y":
    price += 1
    print(f"Your bill for Medium Pizza is ${price}")
  else:
    print(f"Your bill for Medium Pizza is ${price}")
elif size == "L":
  price += 25
  if add_pepperoni == "Y":
    price += 3
  if extra_cheese == "Y":
    price += 1
    print(f"Your bill for Large Pizza is ${price}")
  else:
    print(f"Your bill for Large Pizza is ${price}")

# Angela solution

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your bill is {bill}")

# Build a love calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
# combine both names to a string 
combined_string = (name1 + name2)
# turn string to lower case
lower_combined_string = combined_string.lower()
#look for occurence of TRUE in string
t = lower_combined_string.count("t")
r = lower_combined_string.count("r")
u = lower_combined_string.count("u")
e = lower_combined_string.count("e")
# Add the count. NB: .count() result is integer
true = (t + r + u + e)

#look for occurence of TRUE in string
l = lower_combined_string.count("l")
o = lower_combined_string.count("o")
v = lower_combined_string.count("v")
e = lower_combined_string.count("e")
# Add the count. NB: .count() result is integer
love = (l + o + v + e)
# make result string go as to be able to concatenate
result = str(true) + str(love)
# int of the result for if statements
resultt = int(result)

if resultt < 10 or resultt > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif resultt >= 40 or resultt <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")

# Day 3 final ass - create a treasure island game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("'You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n")
lower_direction = direction.lower()
if lower_direction == "right":
  river = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
  lower_river = river.lower()
  if lower_river == "wait":
    pill = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \"Yellow\", \"red\" or \"blue\"\n")
    lower_pill = pill.lower()
    if lower_pill == "red":
      print("It's a room full of fire. Game Over.")
    elif lower_pill == "blue":
      print("You found the treasure! You Win!")
    elif lower_pill == "yellow":
      print("You enter a room of beasts. Game Over.")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
  elif lower_river == "swim":
    print("Sorry, you've been eaten by hungry crocs. Game Over!")
elif lower_direction == "left":
  print("Oops, you've fallen into pit! you've GAme Over!")



