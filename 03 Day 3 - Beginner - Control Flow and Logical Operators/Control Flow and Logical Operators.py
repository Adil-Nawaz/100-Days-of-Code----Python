# Welcome to the Rollercoaster 1.0
height = int(input("Enter your height in cm: "))
if height>=120:
    print("Ok. You can ride")
else:
    print("Sorry..! You can't ride")

#Odd or even exercise
number = int(input("Enter the number to check if it is Even or Odd: "))
if (number%2==0):
    print(f"The number {number} is Even")
else:
    print(f"The number {number} is Odd")

# Welcome to the Rollercoaster 1.1
height = int(input("Enter your height in cm: "))
if height>=120:
    print("Ok. You can ride")
    age = int(input("Enter your age in years: "))
    if age<12:
        print("You will pay $5")
    elif age <=18:
        print("You will pay $7")
    else:
        print("You will pay $12")
else:
    print("Sorry..! You can't ride")

#BMI Calculator 2.0
weight = float(input("Enter your weight in KGs: "))
height = float(input("Enter your height in meters: "))
BMI = weight / (height**2)
if BMI<18.5:
    print(f"Your BMI is {round(BMI)} & You are underweight")
elif BMI<25:
    print(f"Your BMI is {round(BMI)} & You have normal weight")
elif BMI<30:
    print(f"Your BMI is {round(BMI)} & You are overweight")
elif BMI<35:
    print(f"Your BMI is {round(BMI)} & You are obese")
else:
    print(f"Your BMI is {round(BMI)} & You are clinically obese")

# Welcome to the Rollercoaster 1.2
height = int(input("Enter your height in cm: "))
if height>=120:
    print("Ok. You can ride")
    age = int(input("Enter your age in years: "))
    if age<12:
        pic = input("Do you want to have pictures? Y for Yes and N for No: ")
        if pic=="y":
            print("You will pay $5 + $3 = $8")
        if pic=="n":
            print("You will pay $5")
    elif age <=18:
        pic = input("Do you want to have pictures? Y for Yes and N for No: ")
        if pic=="y":
            print("You will pay $7 + $3 = $10")
        if pic=="n":
            print("You will pay $7")
    else:
        pic = input("Do you want to have pictures? Y for Yes and N for No: ")
        if pic=="y":
            print("You will pay $12 + $3 = $15")
        if pic=="n":
            print("You will pay $12")
else:
    print("Sorry..! You can't ride")

# Welcome to the Rollercoaster 1.2.1
height = int(input("Enter your height in cm: "))
bill=0
if height>=120:
    print("Ok. You can ride")
    age = int(input("Enter your age in years: "))
    if age<12:
        bill=5
    elif age <=18:
        bill=7
    else:
        bill=12
    pic = input("Do you want to have pictures? Y for Yes and N for No: ")
    if pic=="y":
        totalBill = bill + 3
        print(f"You will pay a total bill of ${totalBill}")
    if pic=="n":
        print(f"You will pay a total bill of ${bill}")
else:
    print("Sorry..! You can't ride")
    
#Python Pizza Delivery Program
print("Welcome to Python Pizza Deliveries..!")
size = input("What size of pizza do you want? S, M or L ")
bill = 0
totalBill = 0
grandTotal = 0
pepp_for_S = 2
pepp_for_M_L = 3
ex_cheese_for_any = 1
if size=="s":
    bill = 15
elif size=="m":
    bill = 20
elif size=="l":
    bill = 25
else:
    print("Please enter valid input")

add_pepperoni = input("Do you want to add pepperoni? Y or N ")
if add_pepperoni=="y" and size=="s":
    totalBill = bill + pepp_for_S
elif (add_pepperoni=="y") and (size=="m" or size=="l"):
    totalBill = bill + pepp_for_M_L
else:
    totalBill = bill
extra_cheeze = input("Do you want extra cheez? Y or N ")
if extra_cheeze=="y":
    grandTotal = totalBill + ex_cheese_for_any
    print(f"Your total payment is ${grandTotal}")
else:
    print(f"Your total payment is ${totalBill}")

# Welcome to the Rollercoaster 1.3
height = int(input("Enter your height in cm: "))
bill=0
if height>=120:
    print("Ok. You can ride")
    age = int(input("Enter your age in years: "))
    if age<12:
        bill=5
    elif age <=18:
        bill=7
    elif age >=45 and age<=55:
        bill = 0 
    else:
        bill=12
    pic = input("Do you want to have pictures? Y for Yes and N for No: ")
    if pic=="y":
        totalBill = bill + 3
        print(f"You will pay a total bill of ${totalBill}")
    if pic=="n":
        print(f"You will pay a total bill of ${bill}")
else:
    print("Sorry..! You can't ride")
    
#Welcome to Love Calculator 1.0
print("Welcome to Love Calculator 1.0")
name1 = input("Enter your name: ").lower()
name2 = input("Enter your partner's name: ").lower()
name1Count = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
name1Count2 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
name2Count = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
name2Count2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
totalTrue = name1Count + name2Count
totalLove = name1Count2 + name2Count2
trueLove = int(str(totalTrue) + str(totalLove))
if trueLove < 10 or trueLove>90:
    print(f"Your score is {trueLove} and you go like coke and mentos")
elif trueLove >= 40 and trueLove<=50:
    print(f"Your score is {trueLove} and you are alright together")
else:
    print(f"Your score is {trueLove}")

#Welcome to Love Calculator 1.0.1
print("Welcome to Love Calculator 1.0.1")
name1 = input("Enter your name: ").lower()
name2 = input("Enter your partner's name: ").lower()
combined_name = name1+name2
trueCount = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
loveCount = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e") 
loveScore = int (str(trueCount) + str(loveCount))  #converted a concatenated string into int
if loveScore < 10 or loveScore>90:
    print(f"Your score is {loveScore} and you go like coke and mentos")
elif loveScore >= 40 and loveScore<=50:
    print(f"Your score is {loveScore} and you are alright together")
else:
    print(f"Your score is {loveScore}")

#Exercise 3
print("******** WELCOME TO THE TREASURE ISLAN PROGRAM ********")
print("Your mission is to find the treasure.")
response1 = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\":  ").lower()
if response1 == "left":
    response2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across: ").lower()
    if response2 == "wait":
        response3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if response3 =="yellow":
            print("Congratulations.. You win!")
        elif response3 == "blue":
            print("You enter a room of beasts.. Game Over")
        else:
            print("You enter a room of bombs.. Game over")
    else:
        print("Game over")
else:
    print("Game over")
print("******** THIS IS THE END OF THE PROGRAM PROGRAM ********")