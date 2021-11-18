#
alien_colors = ['green', 'blue', 'red']
for alien_color in alien_colors:
	if alien_color == 'green':
		print(f"sadly, I don't like {alien_color}")
	else:
		print(f"I love {alien_color}\n")

# combining multiple lists. The available_toppings can be a tuple or adjustable linkdepending on the pizza company's menu
available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Now adding {requested_topping}!")
	else:
		print(f"Out of {requested_topping} now!")
print("\nYour Pizza is ready!\n")

# Assignment
usernames = ['Toolz','Ola','admin','Lol','Gala']
firstNames = ["Yusuf"]
for username in usernames:
	if username == 'admin':
		print(f'Hello {username}, would you like to see a status report?')
	else:
		print(f"Hello {username}, thank you for logging in again\n")


# no user list
user_names = []
if user_names:
	value = []
	print(f"adding {value}")
else:
		print("We need more users!")



