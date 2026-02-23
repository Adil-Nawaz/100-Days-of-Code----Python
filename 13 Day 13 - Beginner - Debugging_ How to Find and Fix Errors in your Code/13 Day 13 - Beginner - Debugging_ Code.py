#Debugging

# 1. Describe the  problem
def my_Function():
    for i in range (1,20+1):         #the problem was in range(1,20) because it will never go to 20 range works range(0,n-1)
        if i==20:
            print("You got it")

my_Function()

# 2. Reproduce the bug
from random import randint
dice_imgs = ["1️⃣", "2️⃣","3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0,5)
#randint works for both start and end points but list index start from 0 so index 0 will never be executed & index 6 will
#produce an error of index out of range
print(dice_imgs[dice_num]) 

# 3. Play Computer
year = int(input("What's your year of birth?: "))
#No code written to check year == 1994 execute code step by step like computer
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year >= 1994:
    print("You are a Gen-Z")

# 4. Fix the errors when console gives red underlined erros
age = int(input("How old are you?: "))  #there is also a type error between string and int
if age > 18: 
    print(f"You can drive at {age}.")   #Error tells expected indented block - there should also be a f string 

# 5. Print() is your best friend
pages = 0
word_per_Page = 0
pages = int(input("Number of pages: "))
word_per_Page = int(input("Number of words per page: "))  #it contained error here as word_per_page == int(input())
total_words = pages * word_per_Page
print(total_words)

# 6. Use a debugger

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)       #here b_list.append(new_item) was not rightly indented which caused output only [26]
    print(b_list)

mutate([1,2,3,5,8,13]) 

# 7. Take a break
# 8. Run the code often
# 9. Ask stackoverflow

# Debugging odd or even exercise
number = int(input("Which number do you want to check? : "))
if number %2 == 0:                             #there must be == sign instead of single = sign
    print("This is an even number!")
else:
    print("This is an odd number!")



# Debugging leap year

year = int(input("Which year do you want to check? : "))   #the error contained in type as it was not converted into int
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")



#Debugging FizzBuzz code
for number in range(1, 101):
    if number % 3 == 0 and  number % 5 == 0:   #It contained or instead of and
        print("FizzBuzz")
    elif number % 3 == 0:                    #it contained multiple ifs instead of elif statements
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)