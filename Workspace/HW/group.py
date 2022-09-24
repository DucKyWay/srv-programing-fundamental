print("Welcome to Python Pizza Deliveries!")
size = input("Which pizza size do you want to order? S , M or L = ")
bill = 0
if size == "S":
    bill = 15
    print("You have to pay $", bill)
elif size == "M":
    bill = 20
    print("You have to pay $", bill)
elif size == "L":
    bill = 25
    print("You have to pay $", bill)
else:
    print("Not found size")

add_pepporoni = input("Do you want to add pepporoni? Y or N = ")
if add_pepporoni == "Y":
    if size == "S":
        bill = bill + 2
        print("You have to pay $", bill)
    else:
        bill = bill + 3
        print("You have to pay $", bill)

extra_cheese = input("Do you want to add extra cheese? Y or N = ")
if extra_cheese == "Y":
    bill = bill + 1
    print("You have to pay total$", bill)
else:
    print("You have to pay total $", bill)