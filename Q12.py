# Question 12. A small CLI asks for a quantity. abc and -3 are rejected and the prompt repeats. A positive integer is accepted.


quantity = 0

iscorrect = True
while iscorrect == True:
    try:
        quantity = int(input("Enter the Quantity of the Object: "))
        if quantity<=0:
            raise ValueError("Negative Value not be entered")
        else:
            iscorrect = False
    except ValueError:
        print("You Enter the wrong Quantity type")

print(f"Quantity Entered by user is {quantity}")   
    
    
    