cars = ['pra', 'neo', 'bre', 'ket', 'tod']
for car in cars:
	if car == 'neo':
		print(car.upper())
	else:
		print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
if 'onions' in requested_toppings:
	print('I love onions')


topp = 'sugar'
if topp != 'sugar':
	print("bring the sugar")
else:
	print('fuck Sugar!')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.upper() + ',' + ' you are free to comment.')
	print(f"{user.title()}, you can comment.")

