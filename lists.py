# Olayinka - How to run lists command in Python.also show how toadd String Methods to your lists, modifying lists (replace, add, insert & delete)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2])
print(bicycles[0].title())
print(bicycles[3].upper())
print(bicycles[-2])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


coin_mata = ['Yinka', 'Axis', 'Vic', 'Bisi', 'MJ', 'Wale']
print(coin_mata[-3].title())
coin_mata[0] = 'Baba_Oba'
coin_mata.append('Femi')
print(coin_mata)

sports = []
sports.append('Football')
sports.append('Tennis')
sports.append('judo')
print(sports)

sports.insert(1,'Rugby')
print(sports)

del sports[1]
print(sports)

sports.remove('judo')
print(sports)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)