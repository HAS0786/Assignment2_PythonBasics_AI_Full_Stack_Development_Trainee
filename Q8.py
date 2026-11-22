# Question 8. A month of deposits and withdrawals. Print the running balance and the first day it goes negative. Include a history that never goes negative.

# Positive number means => Adding in account
# Negative number means => Deduct in account
# Zeor number means => No Adding in account

transaction = [2000,4000,-19,-3442,0,111,4239,-43,-13333,7373,2901,-321,3244,0,-8999,2289,38,4343,2233,-3343,322,-4443,23,-3453,-444,24,0,234,555,9303]

negative_balance = [] # Negative balance day-value
negative_balance_day = [] # Negative balance days

positive_history = [] # Days-value, at which no negative balance
positive_history_day = [] # Days, at which no negative balance

zero_balance_history = []  # track Zero Balance Days-value in Month
zero_balance_day = []  # track Zero Balance Days in Month

running_balance = 0

day = 1
for tran in transaction:
    running_balance += tran
    # Running Balance
    print(f"Running Balance in an Account (Day-wise)=> Day {day} is: {running_balance}")
    
    if running_balance < 0:
        negative_balance_day.append(day)
        negative_balance.append(running_balance)
    elif running_balance > 0:
        positive_history_day.append(day)
        positive_history.append(running_balance)
    else:
        zero_balance_day.append(day)
        zero_balance_history.append(running_balance)
    day +=1
        
# Negative Balance History  
if len(negative_balance)<=0:
    print("No Negative Balance history in a month")
else:
    print(f"First Negative Balance day is at {negative_balance_day[0]}rd day and balance-value is {negative_balance[0]}")     

# Positive Balance History  
if len(positive_history)<=0:
    print("No Positive Balance history in a month")
else:
    i = 0
    print("Positive Balance History")
    for postive_bal in positive_history:
        print(f"Day {positive_history_day[i]}:  balance {postive_bal}")
        i+=1


if len(zero_balance_history)<=0:
    print("No Zero Balance history in a month")
else:
    i = 0
    print("Zero Balance History")
    for zero_bal in zero_balance_history:
        print(f"Day {zero_balance_day[i]}:  balance {zero_bal}")
        i+=1
    