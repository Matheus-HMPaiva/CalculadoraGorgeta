<<<<<<< HEAD
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 5:
        bill = 3
        print("Please pay $5.")
    elif age <12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")

else:
=======
<<<<<<< HEAD
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 5:
        bill = 3
        print("Please pay $5.")
    elif age <12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}")

else:
=======
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 5:
        bill = 3
        print("Please pay $5.")
    elif age <12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}")

else:
>>>>>>> fde78a68d0083f4766ea524590ad9ec3daacb33d
>>>>>>> ebabb7e056920f3145612580ec5afd5478cfe223
    print("Sorry, you have to grow taller before you can ride.")