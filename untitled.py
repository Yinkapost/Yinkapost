# Assignment
usernames = ['Toolz','Ola','admin','Lol','Gala']
firstNames = ["Yusuf", "admin"]
for username in usernames:
	if username == 'admin':
		print(f'Hello {username}, would you like to see a status report?')
	else:
		print(f"Hello {username}, thank you for logging in again\n")

print("------------------------------")
# empty list
users = []
if users:
	for user in users:
		print(f'Add {user}')
else:
	print('we need more users!')

print("------------------------------")
#create multiple list and tell those with pre-existing usernames tocreate new ones making sure lists arecase insensitive.
usernames = ['toolz','ola','admin','lol','gala']
usernames = [i.lower() for i in usernames]
new_users = ['Toolz','Ayo','OLa','Bisi','Admin']
for new_user in new_users:
	if new_user.lower() in usernames:
		print(f'{new_user}, you will have to create new username.')
	else:
		print(f'{new_user}, welcome to the platform.')
print('------------------------------------')
# loopingthrough a list of numbers and assigning right suffix
nos = ['1','2','3','4','5','6','7','8','9']
for no in nos:
	if no == '1':
		print(f'{no}st')
	elif no == '2':
		print(f'{no}nd')
	elif no == '3':
		print(f"{no}rd")
	else:
		print(f'{no}th')
