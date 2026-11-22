# Question 4. print(0.1 + 0.2) shows a long float. Build the same bill in paisa (integers) so the receipt never shows that error.

# Rupee
print(0.1+0.2)  #too long floating value

# one Rupee is equal to 100 Paisa
num1 = int(0.1*100) # 10 Paisa
num2 = int(0.2*100) # 20 Paisa
bill = num1+num2
print(f"Your Bill is {bill} paisa")
print(type(bill))
