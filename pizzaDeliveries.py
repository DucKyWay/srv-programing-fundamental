def total_bill():
    print(f"You have to pay ${bill}")

print("-------------------------------------")
print("Welcome to Python Pizza Deliveries!")
print("-------------------------------------")
size = input("Which pizza size do you want to order? S , M or L = ")

price = [15, 20, 25]
bill = 0

if size == "S":
    bill = price[0]
    total_bill()
    print("You choose", size)
elif size == "M":
    bill = price[1]
    total_bill()
    print("You choose", size)
elif size == "L":
    bill = price[2]
    total_bill()
    print("You choose", size)
else:
    print("Not found size")
print("-------------------------------------")

add_pepporoni = input("Do you want to add pepporoni? (y/ n) = ")
if add_pepporoni == "y":
    if size == "S":
        bill+=2
        total_bill()
    elif size == "M":
        bill+=3
        total_bill()
    elif size == "L":
        bill+=3
        total_bill()
else:
    total_bill()
print("-------------------------------------")

extra_cheese = input("Do you want to add extra cheese? (y/ n) = ")
if extra_cheese == "y":
    bill+=1
    total_bill()
else:
    total_bill()
print("-------------------------------------")

print(f"Your actuall bill is ${bill}")