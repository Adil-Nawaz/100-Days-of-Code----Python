import random
print("Welcome to the number guessing game!")
def diffcultyLevel(level):
    if level == "easy":
        return 5
    elif level == "hard":
        return 10
    else:
        print("Wrong choice!")
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")

attempts = diffcultyLevel(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())