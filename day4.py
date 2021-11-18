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
 
print(dirty_dozen[1][3])

