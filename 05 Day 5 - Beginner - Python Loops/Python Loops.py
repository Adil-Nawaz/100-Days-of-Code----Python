
#Simple for loop
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
for fruit in fruits:
    print(fruit)
    print(f"{fruit}'s pie")
for veges in vegetables:
    print(veges)
    print(f"{veges}'s Salan")

#Average height of students calculator
#sample data 180,124,165,173,189,169,146
studentsheights = input("Enter the heights of students separated by comma: ")
listofHeights = studentsheights.split(",")
sum = 0
numberOfStudents = 0
for heights in listofHeights:
    sum += int(heights)
    numberOfStudents += 1
print(f"Heights of students are: {listofHeights}")
print(f"Number of students is: {len(listofHeights)}")
print(f"Average height of students is: {round(sum/numberOfStudents)}")  # can also use sum/len(listofHeights)

#Getting the highest number from the list 1.0
#sample data 78,65,89,86,55,91,64,89
while True:
        numbers= input("Enter the numbers to know highest score separated by comma: ").split(",")
        numbers2 = []

        for i in range(0, len(numbers)):
            numbers2.append(int(numbers[i]))
            #print(type(numbers2[0]))
        numbers2.sort(reverse=True)
        print(f"You entered: {numbers}")
        print(f"The Highest score in the list is: {numbers2[0]}")

        checkagain = input("Want to check again? (y/n) ").lower()
        if checkagain!="y":
            break

#Getting the highest number from the list 1.1
#sample data 78,65,89,86,55,91,64,89
while True:
        numbers= input("Enter the numbers to know highest score separated by comma: ").split(",")
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
            # print(type(numbers[0]))
        print(numbers)
        highestScore = 0
        for score in numbers:
             if score> highestScore:
                  highestScore = score

        print(f"The Highest score in the list is: {highestScore}")

        checkagain = input("Want to check again? (y/n) ").lower()
        if checkagain!="y":
            break

#add numbers from 1 to 100
sum = 0
for number in range(1,100+1):
    sum+=number
print(f"Sum of numbers from 1 - 100 is: {sum}")

#Adding even numbers from 1 to 100
sumOfEvens = 0
for numbers in range(0,100+1):
    if (numbers %2 == 0):
        sumOfEvens+=numbers
print(f"Sum of evens from 1 - 100 is: {sumOfEvens}")

#FizzBuzz Job interview question
for num in range(1,101):
    if (num %3 == 0 and num %5 == 0):
        print("FizzBuzz")
    elif (num %3 == 0):
        print("Fizz")
    elif (num %5 == 0):
        print("Buzz")
    
    else:
        print(num)

print("******** WELCOME TO THE PyPASSWORD GENERATOR PROGRAM ********")
import random
lettersList = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsList = [
'!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
'-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
"'", '"', ',', '.', '<', '>', '/', '?', '\\', '|',
'`', '~'
]

while True:
    letters = int(input("How many letters would you like in your passowrd? "))
    symbols = int(input("How many symbols would you like in your passowrd? "))
    numbers = int(input("How many numbers would you like in your passowrd? "))
    password = ""
#getting random characters from letters
    for char in range(1,letters+1):
        password += random.choice(lettersList)
#getting random characters from symbols
    for sym in range(1,symbols+1):
        password += random.choice(symbolsList)
#getting random characters from numbers
    for num in range(1,numbers+1):
        password += random.choice(numbersList)
    print(password)
    shuffled = "".join(random.sample(password,len(password)))
    print(shuffled)

    runAgain = input("Do you want to run again? (y/n) ").lower()
    if runAgain!="y":
        break

print("******** THIS IS THE END OF THE PROGRAM PROGRAM ********")