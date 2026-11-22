# Question 7. Find the highest mark without max(). Include an all-negative list and a one-item list.

marks = []

number = int(input("How much marks you want to enter: "))     
    
i = 0
while i<number:
    mark = int(input("Enter the Marks (one-by-one): "))    
    marks.append(mark)
    i+=1

# Only print for displaying Numbers:
for mrk in marks:
    print(mrk) 
  
if len(marks) == 0:
    print("No Marks in List")
        
else:    
    highest = marks[0]

    for mark in marks:
        if highest<mark:
            highest = mark

    print(f"Highest Number is: {highest}")    
