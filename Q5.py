# Question 5. Grade a mark: A from 80, B from 65, C from 50, F below 50. Test 49, 50, 64, 65, 79, and 80.

marks = int(input("Enter the Marks (0-100):"))

print(marks)

if marks<0:
    print("Marks not be less than Zero")
elif marks>100:
    print("Marks not be greater than 100 for one Subject")
elif marks>80 and marks<=100:
    print("Grade A")
elif marks>=65 and marks<80:
    print("Grade B")
elif marks>=50 and marks<65:
    print("Grade C")
else:
    print("Grade F")