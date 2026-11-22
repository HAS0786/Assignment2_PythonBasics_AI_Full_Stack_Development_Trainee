# Question 11. A program averages a list and crashes on an empty list with ZeroDivisionError. Handle it with a clear result. Do not hide the error in a bare except.


list_size = int(input("How much numbers you want to Add: "))
numbers = []
total = 0
i=0
while i < list_size:
    number = int(input("Enter the Numbers one-by-one: "))    
    numbers.append(number)
    i+=1
    
for num in numbers:
        total+=num 
length = len(numbers)   
try:
    avg = total/length
    print(avg)
except ZeroDivisionError:
    print("List is Empty and Size 0")

else: # runs when Try block runs without any error
    print("Code runs without any error")
    
finally:
    print("Thanks")
    
    
    
# Bare Except => recieve any kind of error while ZeroDivisionError only when we divide something with zero like 5/0

