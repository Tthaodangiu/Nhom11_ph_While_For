# Define the original prices
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

# Calculate the discount amount and new price for each item
discount_percentage = 60  # 60% off
discount_table = []
for price in original_prices:
    discount = price * (discount_percentage / 100)
    new_price = price - discount
    discount_table.append((price, discount, new_price))
# Display the discount table
print("Original Price\tDiscount\tNew Price")
for item in discount_table:
    original_price = round(item[0], 2)
    discount = round(item[1], 2)
    new_price = round(item[2], 2)
    print(f"{original_price}\t\t{discount}\t\t{new_price}")
    