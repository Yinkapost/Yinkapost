# I will be creating a for loop program to help loopthrough any length of list. Sending message to all at the same time; look at indention errors(syntax, logical)
tours = ['Madrid', 'London', 'NY', 'Doha', 'Rome']
for tour in tours:
	print(tour + '\n')

for tour in tours:
	print(tour.title() + ' is a a city I love.')
	print('I will be going to ' + tour.title() + ' next summer.' + '\n')
print('Next year, I am going to all the cities' + '\n')


foods = ['rice', 'beans', 'bread']
for food in foods:
	print(food.title())
	print('I love eating ' + food.title() + '\n')
print('Food is healthy for the body.')