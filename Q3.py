# Question3. A bill of 5 items gets 10% off, then 17% sales tax, rounded to whole rupees. Also compute tax-then-discount for the same bill.

# Discount = 10%
# Sales Tax = 17
# Task 1: Discount then Sales Tax
# Task 2: Sales Tax then Discount


price_of_items = [] #list of Items_price (enter by user)
discount = 0.10 # 10% => 10/100 = 0.1
sales_tax = 0.17 # 17% => 17/100 = 0.17

# Take input the price of Items
i=1
while i<6:
    items = int(input(f"Enter the Price of Item {i}: "))
    price_of_items.append(items)
    i+=1
    
# Calculate total Price: 
total_price_for_task1 = 0    
total_price_for_task2 = 0    
for item in price_of_items:
    total_price_for_task1+=item
    total_price_for_task2+=item
    
# ================= Task 1 ========================= 
print(f"Total Price without Discount & Sales Tax: {total_price_for_task1}")
# Apply Discount
discounted_price = total_price_for_task1*discount
total_price_for_task1 = total_price_for_task1-discounted_price
print(f"Total Price after Discount: {round(total_price_for_task1)}")
# Now Apply Sales Tax
sales_price = total_price_for_task1*sales_tax    
total_price_for_task1 = total_price_for_task1+sales_price
print(f"Total Price after Sales Tax: {round(total_price_for_task1)}")
    
# ================ Task 2 ==================
print(f"Total Price without Discount & Sales Tax: {total_price_for_task2}")
# Apply Sales Tax
sales_price = total_price_for_task2*sales_tax    
total_price_for_task2 = total_price_for_task2+sales_price
print(f"Total Price after Sales Tax: {round(total_price_for_task2)}")
# Now Apply Discount
discounted_price = total_price_for_task2*discount
total_price_for_task2 = total_price_for_task2-discounted_price
print(f"Total Price after Discount: {round(total_price_for_task2)}")

