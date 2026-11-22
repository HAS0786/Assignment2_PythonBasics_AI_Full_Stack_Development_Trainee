# Question 1. Ask for a birth year and print the age this year. Run it for 3 years the mentor picks.

# Breakdown
# Take the Input Birth Year 
# Then calculate the Age

current_year = 2026
def calculateAge(year):
    # Calculation:
    if year<1899:
        return "Invalid Birth-Year"
    elif year>2026:
       return "Birth-Year not be in Negative"
    elif year==2026:
        return "Your are few months old"
    else:
        calculate_age = current_year-year
        return f"Your are {calculate_age} years old";
# we convert the input into INT (as Input give us String-bydefault)
birthYear = int(input("Enter your Birth Year (e.g: 2010): "))
age = calculateAge(birthYear)
print(age)


