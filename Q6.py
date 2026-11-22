# Question 6. Electricity bill: first 100 units at Rs 10, next 100 at Rs 15, the rest at Rs 25. Test 0, 100, 101, 200, and 350 units.

unit = int(input("Enter the Unit: "))

match unit:
    case unit<=100:
        print(f"Bill for {unit} is: {unit*10} ")
    case unit>100 and unit<=200:
        extra_unit = unit - 100
        total = (100*10)+(extra_unit*15)
        print(f"Bill for {unit} is: {total} ")
    case unit>200
        extra_unit = unit-200
        total = (100*10)+(100*15)+(extra_unit*25)
        print(f"Bill for {unit} is: {total}")
        
        