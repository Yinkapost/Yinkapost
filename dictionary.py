alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

alien_0['height'] = '5ft'
alien_0['size'] = 8
print(alien_0)
print("--------------------------------------")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
       # This must be a fast alien.
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {alien_0['x_position']}")