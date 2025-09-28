"""Exam Eligibility Check
Outline:
Write a program to check whether the student can take an exam or not.
 Students will be allowed only in two conditions:
 If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed.
 If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed."""

medicalcause=input("Does this person have a medical cause ir not,enter yes or no:")
if medicalcause=="yes":
    print("You are allowed for the test")
else:
    attendence=int(input("How many days does this person have attendence:"))
    if attendence>=75:
        print("You are allowed")
    else:
        print("You are not allowed")



"""Electricity bill
Outline:
Write a program to calculate the electricity bill. 
The bill is calculated by checking the number of units consumed. 
Suppose the user is consuming less than 50 units.
 The per-unit cost will be 2.60, and the tax on that bill will be 25.
 If a user is consuming more than 50 but less than 100.
 Then the per-unit cost will be 3.25, and the tax on that bill
will be 35 If the user is coming more than 100 and less than 200.
Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45,
 and the tax is 75"""

def calculate_bill(units):
    if units < 50:
        cost = units * 2.60
        tax = 25
    elif 50 <= units < 100:
        cost = units * 3.25
        tax = 35
    elif 100 <= units < 200:
        cost = units * 5.26
        tax = 45
    else:  
        cost = units * 8.45
        tax = 75
    
    total_bill = cost + tax
    return total_bill


try:
    units_consumed = float(input("Enter the number of units consumed: "))
    if units_consumed < 0:
        print("Units consumed cannot be negative.")
    else:
        final_bill = calculate_bill(units_consumed)
        print(f"The total electricity bill is: ${final_bill:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number.")




"""Customise your ride
Outline:
Write a program to select a ride according to your preference.
 The ride is divided into two major
 categories:
 1. Bike 2. Car And further, bikes and cars
 are divided into 2 subcategories.
   To give the user better selection options."""

ans=input("Pease enter bikes or cars: ")
if ans=="bike":
    print("Pick one company TREK or SPECIALEZED")
    ans1=input("Which one do you choose:")

elif ans=="car":
    print("Pick one company Bugatti or F1")
    ans2=input("Which one do you choose:")
    




