print("SMART CANTEEN MANAGEMENT")

items = ["Idli", "Dosa", "Meals", "Juice"]
prices = [30, 50, 80, 25]
stock = [50, 40, 30, 60]

total_sales = 0

while True:
    print("\nMENU")

    for i in range(len(items)):
        print(i + 1, items[i], "- Rs.", prices[i],
              "- Stock:", stock[i])

    choice = int(input("\nEnter item number (0 to exit): "))

    if choice == 0:
        break

    if choice < 1 or choice > len(items):
        print("Invalid item selection")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity")

    elif quantity > stock[choice - 1]:
        print("Insufficient stock")

    else:
        index = choice - 1

        bill = prices[index] * quantity

        stock[index] -= quantity
        total_sales += bill

        print("\nORDER SUCCESSFUL")
        print("Item:", items[index])
        print("Quantity:", quantity)
        print("Bill Amount: Rs.", bill)

print("\nDAILY SALES REPORT")
print("Total Sales: Rs.", total_sales)

print("\nREMAINING STOCK")

for i in range(len(items)):
    print(items[i], ":", stock[i])
