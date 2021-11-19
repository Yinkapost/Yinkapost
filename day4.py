# # a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"
# #Write your code below this line 👇
# #Hint: Remember to import the random module first. 🎲
# import random
# # game = input("Heads or Tails").lower()

# HorD = random.randint(0, 1)
# if HorD == 0:
#   print("Head")
# elif HorD == 1:
#   print("Tail")
  
# # ass = write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# random_names = random.randint(0, 4)
# if random_names == 0:
#   print(f"{names[0]} will pay for the meal")
# elif random_names == 1:
#   print(f"{names[1]} will pay for the meal")
# elif random_names == 2:
#   print(f"{names[2]} will pay for the meal")
# elif random_names == 3:
#   print(f"{names[3]} will pay for the meal")
# elif random_names == 4:
#   print(f"{names[4]} will pay for the meal")

# # angela solution
# import random
# num_items = len(names)
# random_names = random.randint(0, num_items - 1)
# nam = names[random_names]
# print(f"{nam} will pay today")

# # easier way isusing the random.choice command

# nami = random.choice(names)
# print(f"{nami} will pay today")


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
dirty_dozen[1][3] = "grata"
print(dirty_dozen)

# ass: a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
pos1 = int(position[0]) - 1
pos2 = int(position[1]) - 1
map[pos1][pos2] = "X"

# map[position_string[0] - 1],[position_string[1] - 1] = "x"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

