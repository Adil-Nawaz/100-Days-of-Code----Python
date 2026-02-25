'''
#Scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function {enemies}")
    

increase_enemies()
print(f"Enemies outside function {enemies}")

#Local Scope: exists within functions
def drink_potion():
    potion_Strength = 2
    print(potion_Strength)

drink_potion()
# print(potion_Strength)          it will give name error because the variable is declared inside the function & contains local scope

#Global scope
playerHealth = 10
def drink_potion():
    potion_Strength = 2
    print(playerHealth)   #This variable is accessible inside function as well because it is declared at global scope (outside function)

drink_potion()

#There is no block scope in python like java & c++
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]  #eventhough the variable is defined inside if block it is still accessible outside if block because no block scope

print(new_enemy)


#Modifying global variable
enemies = 1

def increase_enemies():
    global enemies 
    enemies += 2
    print(f"Enemies inside function {enemies}")
    
increase_enemies()
print(f"Enemies outside function {enemies}")

#Python constants and global scope / Global Constants
#Global constants: constants are usually declared as global because we dont want to change anything of constants
#and constants are delcared all uppercase names letters
PI =3.14159
URL = "https:\\"
TWITTER_HANDLE = "Twwitter name"
'''

#The Number guessing game
from ascii_art import logo

#Logo text     Ogre
print(logo)
import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 - 100")
randomNumber = random.randint(1,100)
print(randomNumber)
def diffcultyLevel(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Wrong choice!")

def Guess(num, number):
    if num < number:
       print("Too low.\nGuess again.")
    elif num > number:
        print("Too high.\nGuess again.")
    else:
        print("You guessed right.\nYou won!")

attempts = diffcultyLevel(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
print(f"You have {attempts} attempts remaining to guess the number.")

numGuess=0
while numGuess != randomNumber:
    numGuess = int(input("Make a guess: "))
    Guess(num=numGuess, number=randomNumber)
    if numGuess != randomNumber and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts-=1
    elif attempts <= 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        print("Game over!")
        break
    

    