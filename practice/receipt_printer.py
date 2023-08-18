def print_receipt(item, price):
    print(f"{item:12} ${price:.2f}")


items = [("Apple", 0.50), ("Banana", 0.25), ("Bread", 2.00), ("Milk", 1.50)]

items.append(["Pear", 1.2])

print("Welcome to the Grocery Store")
print("----------------------------")
print("Receipt".center(30))
print("----------------------------")

total = 0.0

for item, price in items:
    print_receipt(item, price)
    total += price

print("----------------------------")
print("----------------------------")
print("Total".ljust(13), end='')

print(f"${total}")
