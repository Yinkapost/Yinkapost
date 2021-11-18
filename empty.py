
# EXTENSION OF THE NESTED IF EQUATION
age = int(input("How old are you?\n"))
height = int(input("How tall are you?\n"))
bill = 0
if height >= 180:
    if age < 5:
        bill += 6
        print(f"Your ticket price is ${bill}")
    elif age <= 18:
        bill += 21
        print(f"Your ticket price is ${bill}")
    else:
        bill += 50
        print(f"Your ticket price is ${bill}")
        
    photos = input("Want photos? Y or N\n")
    if photos == "Y":
        bill += 3
    print(f"Your new bill is ${bill}")     
else:
    print("Sorry, you cant ride.")
