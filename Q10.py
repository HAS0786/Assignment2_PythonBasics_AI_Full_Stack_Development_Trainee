# Question 10. Split the bill into subtotal, discount, tax, and total. Each function is tested on its own.

def subtotal(price):
    subtotal = 0
    for item in price:
        subtotal+=item
    return subtotal   
def discount(bill):
    discount = 0.10
    discounted_price = bill*discount
    
    return bill-discounted_price

def salestax(bill):
    sales_tax = 0.17
    sales_price = bill*sales_tax    
    return bill+sales_price
    
    
price_of_items = [] #list of Items_price (enter by user)
i = 1
while i<6:
    items = int(input(f"Enter the Price of Item {i}: "))
    price_of_items.append(items)
    i+=1

# calling Functions one-by-one

sub_total = subtotal(price_of_items)
print(f"Subtotal is {round(sub_total)}")
sales_tax = salestax(sub_total)
print(f"Price after Sale-tax is {sales_tax}")
total = discount(sales_tax)

print(f"Total Price is {round(total)}")

