# Assignment2_PythonBasics_AI_Full_Stack_Development_Trainee
# Week 2 – Python Programming Fundamentals

**Total Marks:** 100 Points
**Deadline:** Sunday Evening

## Assignment Instructions

- Write a short breakdown of each problem before writing code.
- Each function must return a value rather than only printing it.
- Tests can be written using plain Python `assert` statements this week.
- Test all required examples and boundary cases.
- Make sure you understand your logic and can explain your approach.

---

## 1. Variables, Types, and Input

### Question 1: Calculate Age

Ask the user for their birth year and print their age this year.

Run the program for 3 different years selected by the mentor.

**Pass Criteria:**

- All ages are calculated correctly.
- Explain why `input()` must be converted into a number before performing arithmetic.

### Question 2: Shop Items Total

Store the price and quantity of 3 shop items and calculate their total cost.

Every variable name must describe its value.

Example: `price_rice`, not `a`.

**Pass Criteria:**

- The calculated total matches a manual calculation.

---

## 2. Arithmetic and Money

### Question 3: Bill with Discount and Sales Tax

A bill contains 5 items.

Calculate:

1. Total price before discount and tax.
2. Apply a 10% discount.
3. Apply 17% sales tax to the discounted amount.
4. Round the final amount to whole rupees.
5. Also calculate the bill using tax first and discount afterward.

**Pass Criteria:**

- Both calculation orders match the mentor's 3 bills.
- Explain why changing the order changes the intermediate results.

### Question 4: Floating-Point Precision

Observe the result of:

`print(0.1 + 0.2)`

Build the same bill calculation using integer paisa instead of floating-point arithmetic.

Remember: 1 rupee = 100 paisa.

**Pass Criteria:**

- All 3 bills match to the rupee.
- Explain the floating-point precision error in one sentence.

---

## 3. Conditions

### Question 5: Grade Calculator

Grade a student's marks according to these conditions:

| Marks        | Grade |
| ------------ | ----- |
| 80 and above | A     |
| 65–79        | B     |
| 50–64        | C     |
| Below 50     | F     |

Test these values:

`49, 50, 64, 65, 79, 80`

**Pass Criteria:**

- All 6 boundary cases produce the correct grade.

### Question 6: Electricity Bill Calculator

Calculate an electricity bill using these rates:

| Units           |            Rate |
| --------------- | --------------: |
| First 100 units | Rs. 10 per unit |
| Next 100 units  | Rs. 15 per unit |
| Remaining units | Rs. 25 per unit |

Test these values:

`0, 100, 101, 200, 350`

**Pass Criteria:**

- All 5 bills match a manual calculation.

---

## 4. Loops and Lists

### Question 7: Find the Highest Mark

Find the highest mark in a list without using Python's built-in `max()` function.

Include:

- An all-negative list.
- A one-item list.
- An empty list.

**Pass Criteria:**

- Both non-empty test cases produce the correct highest mark.
- An empty list returns a clear message.

### Question 8: Monthly Deposits and Withdrawals

Create a month of deposit and withdrawal transactions.

Requirements:

- Print the running balance after each transaction.
- Identify the first day when the balance becomes negative.
- Include a separate transaction history where the balance never goes negative.

**Pass Criteria:**

- The first negative-balance day is identified correctly.
- The never-negative history is handled properly and produces a clear result instead of crashing.

---

## 5. Functions

### Question 9: Grade Function

Create a function:

`grade(mark)`

Requirements:

- Accept a student's marks.
- Return the corresponding letter grade.
- Do not print inside the function.
- Use the same grading bands as Question 5.

Test these values:

`49, 50, 64, 65, 79, 80`

**Pass Criteria:**

- All 6 boundary calls return the correct grade.
- Tests must check the function's return value.

### Question 10: Bill Calculation Using Functions

Split the bill calculation into four components:

1. Subtotal
2. Discount
3. Tax
4. Total

Each function must be tested independently.

**Pass Criteria:**

- Every function works correctly when tested on its own.
- The final total matches Question 3.

---

## 6. Errors and Input Validation

### Question 11: Handle ZeroDivisionError

A program calculates the average of a list but crashes when the list is empty because of `ZeroDivisionError`.

Requirements:

- Handle the empty-list situation.
- Display a clear result.
- Do not hide errors using a bare `except`.

**Pass Criteria:**

- An empty list displays a clear message.
- A normal list still calculates and returns the correct average.

### Question 12: Quantity Input Validation

Create a small command-line program that asks the user for a quantity.

Requirements:

- Reject `abc` because it is not an integer.
- Reject `-3` because a quantity must be positive.
- Repeat the prompt after invalid input.
- Accept a positive integer.

**Pass Criteria:**

- Both invalid inputs are rejected without crashing.
- The value `4` is accepted.

---

## Assignment Completion Checklist

- [x] Question 1 – Variables, types, and input
- [x] Question 2 – Shop items total
- [x] Question 3 – Discount and sales tax
- [x] Question 4 – Floating-point precision
- [x] Question 5 – Conditions and grading
- [x] Question 6 – Electricity bill
- [x] Question 7 – Highest mark using loops
- [x] Question 8 – Running balance
- [x] Question 9 – Grade function
- [x] Question 10 – Bill calculation functions
- [x] Question 11 – Exception handling
- [x] Question 12 – Input validation

---

**Week 2 Goal**

Build a strong foundation in Python programming fundamentals by practicing variables, data types, arithmetic, conditions, loops, lists, functions, exception handling, and input validation.

**Total: 12 Questions | 100 Points**
