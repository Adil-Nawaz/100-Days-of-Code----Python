#Functions with outputs
#Changing case of Name using function
def format_name(first, last):
    f_name = first.title()
    l_name = last.title()
    return f_name +" "+ l_name

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
formatted_Name = format_name(first=firstName, last=lastName)
print(formatted_Name)


#Multiple return values
def format_name(first, last):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    f_name = first.title()
    l_name = last.title()
    return f_name +" "+ l_name

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
formatted_Name = format_name(first=firstName, last=lastName)
print(formatted_Name)


#Leap Year 1.1 Days in month exercise
print("Welcome to Days in a month finder program!")  #ExerciseCode
def leapYearChecker(year):
    """This function takes year as input and returns true for leap year and false for non-leap year"""
    divide_by_4 = year % 4
    divide_by_100 = year % 100
    divide_by_400 = year % 400
    if divide_by_4 != 0:
        return False
    elif divide_by_100 != 0:
        return True
    elif divide_by_400 ==0:
        return True
    else:
        return False

def days_in_month(year, month):
    """This function takes year and month as int and returns the value of days in specific month entered as input"""
    leapFinder = leapYearChecker(year)
    month_Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapFinder == False:
         return month_Days[month-1]
    elif leapFinder==True and month == 2:
        return 29
    elif leapFinder == True and month != 2:
        return month_Days[month-1]
    else:
        return "error"

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days  = days_in_month(year,month)
print(f"The days in {month} month in year {year} are {days}")


from  asciiart import logo, image
print(logo + image)
import os
#Functions
def add(n1, n2):
    """takes 2 int variables as input and returns sum of them"""
    return n1+n2
def subtract(n1, n2):
    """takes 2 int variables as input and returns subtraction of them"""
    return n1-n2
def divide(n1, n2):
    """takes 2 int variables as input and returns division of them"""
    return n1/n2
def multiply(n1, n2):
    """takes 2 int variables as input and returns multiplication of them"""
    return n1*n2
#Operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
#Inputs
def calculator():
    num1 = int(input("Enter the number: "))
    should_continue = True
    while should_continue:
        for keys in operations:
            print(keys)
        operation_Symbol = input("Pick an operation ")
        num2 = int(input("Enter the next number: "))
        calculation = operations[operation_Symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_Symbol} {num2} = {answer}")
        next = input("Would you like to perform another operation? type y for yes, type e to stop and type n to start new calculation ")
        if next=="y":
            num1 = answer
        elif next=="n":
            calculator()
        else:
            should_continue = False


calculator()



