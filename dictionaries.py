alien = {'name': 'Joe'}
print(alien.get('name'))
alien['age'] = 4
print(alien['age'])

# press Enter after the dico bracket, then press space 4 times. Now every key-value pair will be automatically indented
courses = {
        'ola': 'Big',
        'taye': 'Small',
        'tola': 'Tight',
}

olas = courses['ola'].upper()
print(f"Ola's fav is {olas}.")

# Using get() method instead of [] to retrieve value. enables you to print a message when the key is not in the dictionary
cour = courses.get('ade', 'No Ade in this list')
print(f'{cour}')

#
buddy = {
             'first_name': 'Ola',
             'last_name': 'yinka',
             'age': 29,
             'city': 'lagos'
             }
print(buddy.get('first_name'))
print(buddy.get('last_name'))
print(buddy.get('age'))
print(buddy.get('city'))


fav_number = {
        'Ope': 3,
        'Ade': 8,
        'Eja': 7,
        'Ire': 5,
        'Uba': 9,
}
# does not work fav_number = [i.lower() for i in fav_number]
ope_fave = fav_number.get('Ope')
print(f"Ope's favorite number is {ope_fave}.")
        
# add a new item to dictionary
fav_number['Tope'] = 12
print(fav_number)

# delete key-value pair from dictionary
del fav_number['Ade']
print(fav_number)

# This technique is pretty cool: by changing one value in the player's dictionary, you can change the overall behavior of the player
player = {
        'x_position': 0,
        'y_position': 2,
        'speed': 'medium',
}
if player.get('speed') == 'slow':
    x_increment = 1
elif player.get('speed') == 'medium':
    x_increment = 2
else:
    x_increment = 3
print(x_increment)
    
player['x_position'] = player['x_position'] + x_increment
print(player.get('x_position'))
player['speed'] = 'slow'
print(player)
print(player.get('x_position'))

#
fav_number = {
        'Ope': 3,
        'Ade': 8,
        'Eja': 7,
        'Ire': 3,
        'Uba': 9,
}
# loop through a dic for content
for key, value in fav_number.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}\n')
    
# to loop through all the list and print individual messages for each key,value
for key, value in fav_number.items():
        print(f"{key.upper()}'s favorite number is {value}.\n")   
# you can also loop through a dictionary and print just the key or just the value
for key in fav_number.keys():
        print(key.upper())
for numbers in fav_number.values():
        print(numbers)

# use for and if method to loop through a dictionary to print special message to your friends`
friend = ['Eja', 'Uba']
for key, value in fav_number.items():
        print(f"Hi {key.title()}")
        
        if key in friend:
                print(f"\t{key}, I see your favorite number is {value}")
 # print a message for someone not in the dictionary
if 'yinka' not in fav_number.keys():
         print("Yinka, drop your number.\n")
# you can aLSO GET THE value by using .values imstead of .item
for value in fav_number.values():
        print(value)   
print('------------------------------------')
# to avoid repetiton of values or set, put the for-method in sets    
for value in set(fav_number.values()):
        print(value)
