#using the if-elif-else structure to test more than 2 possible situations
age = 60
if age < 3:
	print('Your fee is $0')
elif age < 18:
	print('Fee is $12')
elif age < 22:
	print('Fee is $222')
else:
	print('Fee is $110')

		
# You can also use variables to bypass the admission price within the if-elif-else block
age = 20
if age < 3:
	price = 0
elif age < 18:
	price = 12
elif age < 22:
	price = 222
else:
	price = 110
print(f"Your fee is ${price}.")

# you can also omit the else block and replace with a very specific elif as last block.

age = 60
if age < 3:
	price = 0
elif age < 18:
	price = 12
elif age < 22:
	price = 222
elif age >= 20:
	price = 110
print(f"Your transaction fee is ${price}.")

# Alien assignment
alien_color = ['green', 'blue', 'red']
if 'green' in alien_color:
	print('\nPlayer 1 has earned 5points.')

if 'black' in alien_color:
	print("\nYou lost")
else:
	print("\nYou won\n")

for value in alien_color:
	if value == 'green':
		print(value.upper())
	else:
		print(value.title())

# “Turn your if-else chain into an if-elif-else chain.”
alien_color = ['green', 'blue', 'red']
if 'brown' in alien_color:
	print('You are qualified.')
elif 'yellow' in alien_color:
	print('I am qualified.')
elif 'red' in alien_color:
	print('Go Home!\n')

# “an if-elif-else chain that determines a person’s stage of life. ”
age = 4
if age < 2:
	ager = 'a baby'

elif age <= 4:
		ager = 'a toddler'

else:
	ager = 'an adult'
print(f"This person is {ager}.\n")

# HOW TO USE IF STATEMENTS WITH LISTS FOR SIMPLE ANDCOMPLEX REQUESTS. remember to print value(alien_color) and not the list variable (alien_colorS)
alien_colors = ['green', 'blue', 'red']
for alien_color in alien_colors:
	print(f"one of your favorite is {alien_color}.")

print('\nThat is the list\n')

	#print value and not variable to have separate lists.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
       print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

#
alien_colors = ['green', 'blue', 'red']
for alien_color in alien_colors:
	if alien_color == 'green':
		print(f"sadly, I don't like {alien_color}")
	else:
		print(f"I love {alien_color}")
print("That is that!\n")

# checking empty list if if-else 
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
         print(f"add {requested_topping}")
else:
	print('are you sure?\n')

	# no user list
user_names = []
if user_names:
	for value in user_names:
		print(f"adding {value}")
else:
		print("We need more users!")

