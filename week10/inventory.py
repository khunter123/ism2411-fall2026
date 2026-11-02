# REFLECTION
# 1. Most surprising thing about Python lists:
#    It was weird that .sort() changes the original list right away instead of making a copy. If you aren't paying attention, you can accidentally lose your original order.
#
# 2. Business situation where a list would beat Excel:
#    A list would be useful in a business situation where you need to store and manipulate a collection of items, such as an inventory of products. You can easily add, remove, and sort items without the overhead of managing a spreadsheet.

# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are immutable, which makes them useful for coordinates because the values can't be changed by accident.")
print(coords)

# Exercise 6
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
print("Total:", total)
print("Count:", count)
print("Average:", total / count)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))