tours = ['Madrid', 'London', 'NY', 'Doha', 'Rome']
print("the first three cities are: ")
print(tours[:3])

print('\n'"two cities in the middle are: ")
print(tours[1:4])

print('\n'"the last three cities are: ")
print(tours[2:])


private_tours = tours[:]
tours.append('Lagos')
print(tours)
private_tours.append('Abuja')
print(private_tours)	