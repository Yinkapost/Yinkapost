# Unlike lists, Tuples cant be edited but you can overwrite a touple
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
print(dimensions)

#
# no user list
user_names = []

if user_names:
	for value in user_names:
		print(f"adding {value}")
	else:
		print("We need more users!")