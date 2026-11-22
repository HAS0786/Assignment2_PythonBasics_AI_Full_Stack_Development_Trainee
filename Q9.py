# Question 9. grade(mark) returns the letter. It does not print. It uses the same bands as problem 5.

def grade(marks):
    if marks>80 and marks<=100:
        return ("Grade A")
    elif marks>=65 and marks<80:
        return "Grade B"
    elif marks>=50 and marks<65:
        return "Grade C"
    else:
        return "Grade F"
        
        
marks = int(input("Enter the Marks (0-100): "))

if marks<0:
    print("Marks not be less than Zero")
elif marks>100:
        print("Marks not be greater than 100 for one Subject")
else:
    grade = grade(marks)
    print(grade)