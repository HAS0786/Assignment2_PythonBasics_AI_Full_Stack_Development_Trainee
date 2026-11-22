# Question 7. Find the highest mark without max(). Include an all-negative list and a one-item list.

marks = []

if len(marks) == 0:
    print("No Marks in List")
    
number = int(input("Tell me how much marks you want to enter: "))    
i = 0
while i<number:
    mark = int(input("Enter the Marks (one-by-one): "))    
    marks.append(mark)
    i+=1

for mk in marks:
    print(mk)