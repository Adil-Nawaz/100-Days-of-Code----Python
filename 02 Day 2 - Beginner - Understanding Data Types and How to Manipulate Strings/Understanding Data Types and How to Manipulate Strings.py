#Life in days, weeks and months
age = int(input("Enter your current age in years: "))
if age<90:
    lifeLeftinYears = 90-age
    in_days = lifeLeftinYears*365
    in_weeks = lifeLeftinYears*52
    in_months = lifeLeftinYears*12
    print(f"You have {in_days} days or {in_weeks} weeks or {in_months} months or {lifeLeftinYears} years left")
    
else:
    print("You have lived a long life dude..!")

#BMI Calculator
weight = float(input("Enter your weight in KGs: "))
height = float(input("Enter your height in meters: "))
bMI = weight / (height**2)
print(f"Your BMI is {round(bMI,2)}")

#Adding a 2 digit number
number = input("Enter a 2 digit number: ")
digit1 = int(number[0])
digit2 = int(number[1])
print(f"Sum of 2 digit number is: {digit1+digit2}")

#Subscripting
print("Hello"[0])

print("******** WELCOME TO THE TIP CALCULATOR PROGRAM ********")
totalBill = float(input("What was the total bill? $"))
bill_to_split = int(input("How many people to split the bill? "))
tip_Percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
if tip_Percent==10 or tip_Percent==12 or tip_Percent==15:
    total_Tip = (tip_Percent/100)* totalBill
else:
    print("Enter the value from 10, 12 or 15")
bill_grand_Total = totalBill + total_Tip
bill_per_person = bill_grand_Total / bill_to_split
print(f"Each Person should pay: ${round(bill_per_person,2)}")

print("******** THIS IS THE END OF THE PROGRAM PROGRAM ********")


