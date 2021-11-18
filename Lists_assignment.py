# I am running a program toinvite 3 people to my party. Then replacedone person that couldnt make it. then add 3 more people. Ex on page 46-47-50
party = ['Ola', 'Ayo', 'Ade']
print(party)

message = "I will like to invite " + party[0] + " to my party"
print(message)

mesage = "I will like to invite " + party[-1] + " to my party"
print(mesage)

messag = "I will like to invite " + party[1] + " to my party"
print(messag)

not_coming = party.pop(2)
print(not_coming) 

message = not_coming + " cannot make it to the party"
print(message)

print(party)
party.append('Bisi')
print(party)

party.insert(0, 'Tade')
party.insert(3, 'Fola')
party.append('oba')
print(party)

tade_ex = party.pop(0)
ola_ex = party.pop(1)
ayo_ex = party.pop(2)
oba_ex = party.pop(-1)
print(party)

mes = "You are no longer invited to the party, " + tade_ex + "."
print(mes) 

print("You are still invited "  + party[0])

del party[0]
print(party)
del party[0]
print(party)


tour = ['Oyo', 'Edo', 'Ife', 'Ogun', 'Abia']
print(tour)

print(sorted(tour))
print(tour)

print(sorted(tour, reverse=True))

len(tour)
print(len(tour))


city = ['Madrid', 'London', 'NY', 'Doha', 'Rome']
print(city)

print(sorted(city))
print(city)

print(sorted(city, reverse=True))
print(city)

city.reverse()
print(city)

city.reverse()
print(city)

city.sort()
print(city)

city.sort(reverse=True)
print(city)

print(len(city))