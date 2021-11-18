
coin_mata = ['Yinka', 'Axis', 'Vic', 'Bisi', 'MJ', 'Wale']
print(coin_mata[2].upper())
message = "The members of cm are " + (coin_mata[0]) + ", " + (coin_mata[1]) + ", " + (coin_mata[2]) + " & " + (coin_mata[3]) + "."
print(message)

coin_mata = ['Yinka', 'Axis', 'Vic', 'Bisi', 'MJ', 'Wale']
print(coin_mata[-3])
coin_mata[0] = 'Baba_Oba'
print(coin_mata)
coin_mata.insert(3, 'femi')
print(coin_mata)

del coin_mata[0]
print(coin_mata)

popped_coin_mata = coin_mata.pop()
print(coin_mata)
print(popped_coin_mata)

coin_mata.append('Yinka')
coin_mata.append('Wale')
print(coin_mata)

coin_mata.insert(0, 'Baba Oba')
print(coin_mata)

coin_mata.pop(-2)
print(coin_mata)
