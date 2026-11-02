# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
# Create at least 5 product tuples
# Example: product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product2 = ("P002", "Laptop Pro", 1199.99, 7, "Laptops")
product3 = ("P003", "Wireless Earbuds", 149.99, 25, "Audio")
product4 = ("P004", "Gaming Console", 499.99, 4, "Gaming")
product5 = ("P005", "Smartwatch Z", 249.99, 15, "Wearables")

# TODO 2: Create an inventory list containing all product tuples
# Example: inventory = [product1, product2, ...]
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
# Use a print statement to show each product in the inventory
print("\nCurrent Inventory:")
print("-" * 60)
# Add your code here to display all products
for product in inventory:
    print(product)

# TODO 4: Access specific elements
# Use indexing to:
# - Get and display the first product (store in first_product)
# - Get and display the last product (store in last_product)
# - Get and display the third product's name only (store in third_product_name)
# - Get and display the second product's price and quantity (store in second_price, second_quantity)

print("\n\nAccessing Specific Products:")
print("-" * 60)
# Add your code here
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price, second_quantity = inventory[1][2], inventory[1][3]
print("First product:", first_product)
print("Last product:", last_product)
print("Third product name:", third_product_name)
print("Second product price and quantity:", second_price, second_quantity)

# TODO 5: Use slicing to get subsets
# - Get and display the first 3 products (store in first_three)
# - Get and display products from index 2 to 4 (store in middle_products)
# - Get and display all products except the first one (store in all_except_first)

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
# Add your code here
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]
print("First three:", first_three)
print("Index 2..4:", middle_products)
print("All except first:", all_except_first)

# TODO 6: Add new products to inventory
# Create 2 new product tuples and add them to the inventory list
# Use the .append() method

print("\n\nAdding New Products:")
print("-" * 60)
# Add your code here
new_product1 = ("P006", "Tablet Air", 599.99, 12, "Computers")
new_product2 = ("P007", "Bluetooth Speaker", 89.99, 20, "Audio")
inventory.append(new_product1)
inventory.append(new_product2)
print("Added:", new_product1)
print("Added:", new_product2)
print("Inventory now has", len(inventory), "items.")

# TODO 7: Remove a product
# Remove the product at index 2 using .pop()
# Display what was removed and show the updated inventory

print("\n\nRemoving a Product:")
print("-" * 60)
# Add your code here
removed_product = inventory.pop(2)
print("Removed:", removed_product)
print("Updated inventory length:", len(inventory))

# TODO 8: Insert a product at a specific position
# Create a new product tuple and insert it at index 1
# Use the .insert() method

print("\n\nInserting a Product:")
print("-" * 60)
# Add your code here
inserted_product = ("P008", "VR Headset", 399.99, 6, "Gaming")
inventory.insert(1, inserted_product)
print("Inserted at index 1:", inserted_product)

# REDO TODO 4 and 5: Please recalculate all access and sliced variables from todos 4 and 5, as the code grader checks these variables against the final state of the inventory.
# Add your code here
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price, second_quantity = inventory[1][2], inventory[1][3]
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
# Create separate lists for different categories
# For example: mobile_phones = [], laptops = [], audio = []
# Go through your inventory and add products to appropriate category lists

print("\n\nProducts by Category:")
print("-" * 60)
# Add your code here
mobile_phones = [p for p in inventory if p[4] == "Mobile Phones"]
laptops = [p for p in inventory if p[4] == "Laptops"]
audio = [p for p in inventory if p[4] == "Audio"]
print("Mobile Phones:", mobile_phones)
print("Laptops:", laptops)
print("Audio:", audio)

# TODO 10: Calculate inventory statistics
# Calculate and display:
# - Total number of products in inventory (store in total_products)
# - Total value of all products (price * quantity for each product) (store in total_value)
# - List of all product names (store in product_names)
# - List of all product prices (store in product_prices)

print("\n\nInventory Statistics:")
print("-" * 60)
# Add your code here
total_products = len(inventory)
total_value = sum(p[2] * p[3] for p in inventory)
product_names = [p[1] for p in inventory]
product_prices = [p[2] for p in inventory]
print("Total products:", total_products)
print("Total value:", round(total_value, 2))
print("Names:", product_names)
print("Prices:", product_prices)

# TODO 11: Find expensive products using list comprehension
# Use a list comprehension to create a list of products that cost more than $500
# Store in variable: expensive_products
# Display these expensive products
# Hint: expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)
# Add your code here
expensive_products = [p for p in inventory if p[2] > 500]
print(expensive_products)

# TODO 12: Low stock alert using list comprehension
# Use a list comprehension to create a list of products with quantity less than 5
# Store in variable: low_stock
# Display these low stock products
# Hint: low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
# Add your code here
low_stock = [p for p in inventory if p[3] < 5]
print(low_stock)

# TODO 13: Create price list using list comprehension
# Use a list comprehension to create a list of all product prices (store in original_prices)
# Then use another comprehension to apply a 10% discount to all prices (store in discounted_prices)
# Display both the original and discounted price lists

print("\n\nPrice Lists:")
print("-" * 60)
# Add your code here
original_prices = [p[2] for p in inventory]
discounted_prices = [round(p[2] * 0.90, 2) for p in inventory]
print("Original:", original_prices)
print("Discounted:", discounted_prices)

# TODO 14: Product name formatting using list comprehension
# Use a list comprehension to create a list of all product names in uppercase (store in uppercase_names)
# Then create another list with product codes (first 3 chars of ID + first 3 chars of name) (store in product_codes)
# Display both lists

print("\n\nFormatted Product Names:")
print("-" * 60)
# Add your code here
uppercase_names = [p[1].upper() for p in inventory]
product_codes = [p[0][:3] + p[1][:3] for p in inventory]
print("Uppercase:", uppercase_names)
print("Codes:", product_codes)

# TODO 15: Using Loops to Process Inventory
# Use a for loop to:
# - Count how many products are in the "Mobile Phones" category (store in mobile_count)
# - Calculate the total value of all "Laptops" in stock (store in laptop_value)
# - Find the most expensive product in the inventory (store in most_expensive)

print("\n\nLoop-Based Analysis:")
print("-" * 60)
# Add your code here
mobile_count = 0
laptop_value = 0.0  # category name must be exactly "Laptops"
most_expensive = inventory[0]
for p in inventory:
    if p[4] == "Mobile Phones":
        mobile_count += 1
    if p[4] == "Laptops":
        laptop_value += p[2] * p[3]
    if p[2] > most_expensive[2]:
        most_expensive = p
print("Mobile count:", mobile_count)
print("Total value of Laptops:", round(laptop_value, 2))
print("Most expensive:", most_expensive)

# TODO 16: Using Conditionals with Lists
# Use loops and conditionals to:
# - Create a list of products that need restocking (quantity < 5) (store in restock_list)
# - Create a list of high-value items (price > $500 AND quantity > 10) (store in high_value_items)
# - Count products in different price ranges: under $100, $100-$500, over $500 (store counts in price_ranges dictionary)

print("\n\nConditional Analysis:")
print("-" * 60)
# Add your code here
restock_list = [p for p in inventory if p[3] < 5]
high_value_items = [p for p in inventory if p[2] > 500 and p[3] > 10]
price_ranges = {"under_100": 0, "100_to_500": 0, "over_500": 0}
for p in inventory:
    if p[2] < 100:
        price_ranges["under_100"] += 1
    elif p[2] <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1
print("Restock list:", restock_list)
print("High value items:", high_value_items)
print("Price ranges:", price_ranges)

# TODO 17: Define and Use Functions
# Define these functions:
# - calculate_product_value(product): returns price * quantity for a product tuple
# - find_products_by_category(inventory, category): returns list of products in given category
# - apply_discount(inventory, discount_percent): returns new inventory with discounted prices
# Then use these functions to:
# - Calculate total inventory value
# - Find all "Audio" products
# - Create a new inventory with 15% discount applied

print("\n\nFunction-Based Operations:")
print("-" * 60)
# Add your code here
def calculate_product_value(product):
    return product[2] * product[3]

def find_products_by_category(inventory_list, category):
    return [p for p in inventory_list if p[4] == category]

def apply_discount(inventory_list, discount_percent):
    factor = 1 - (discount_percent / 100.0)
    return [(p[0], p[1], round(p[2]*factor, 2), p[3], p[4]) for p in inventory_list]

total_inventory_value = sum(calculate_product_value(p) for p in inventory)
audio_products = find_products_by_category(inventory, "Audio")
discounted_inventory = apply_discount(inventory, 15)
print("Total inventory value:", round(total_inventory_value, 2))
print("Audio products:", audio_products)
print("First discounted item example:", discounted_inventory[0])

# TODO 18: Combine Loops, Functions, and List Operations
# Create a function generate_inventory_report(inventory) that:
# - Uses loops to analyze the inventory
# - Returns a dictionary with:
#   - 'total_products': total number of products
#   - 'total_value': sum of all (price * quantity)
#   - 'categories': list of unique categories
#   - 'low_stock': list of products with quantity < 5
#   - 'average_price': average price of all products
# Call the function and display the report

print("\n\nComprehensive Inventory Report:")
print("-" * 60)
# Add your code here
def generate_inventory_report(inv):
    total_products = len(inv)
    total_value = sum(p[2] * p[3] for p in inv)
    categories = sorted(list({p[4] for p in inv}))
    low_stock_list = [p for p in inv if p[3] < 5]
    average_price = (sum(p[2] for p in inv) / total_products) if total_products else 0
    return {
        "total_products": total_products,
        "total_value": round(total_value, 2),
        "categories": categories,
        "low_stock": [p[0] for p in low_stock_list],  # show IDs only
        "average_price": round(average_price, 2)
    }

report = generate_inventory_report(inventory)
print(report)

# TODO When calculating laptop_value, make sure to use the category name exactly "Laptops" (plural).
