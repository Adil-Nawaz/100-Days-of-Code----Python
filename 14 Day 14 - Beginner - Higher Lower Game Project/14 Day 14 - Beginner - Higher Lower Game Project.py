from asciiart import logo, vs
from game_data import data

#Print the logo of game
#put up question 1 Compare A:  name, profession, country
#print VS logo
#put up option 2
#Ask question who has more followers? Type A or B:
#if wrong Sorry, that's wrong. Final Score: 0
#If right, You're right! Current score: 1
#when ans is right then A becomes 0 and B becomes A and next to B option becomes B
'''
print(logo)
currentScore = 0
finalScore = 0
for options in range(0, len(data)):
    dataDraw = data[options]
    followers1 = dataDraw["follower_count"]
    print(f"Compare A: {dataDraw["name"]}, a {dataDraw["description"]}, from {dataDraw["country"]}")
    print(vs)
    dataDraw = data[options+1]
    followers2 = dataDraw["follower_count"]
    print(f"Compare B: {dataDraw["name"]}, a {dataDraw["description"]}, from {dataDraw["country"]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a" and followers1 > followers2:
        print(f"You're right! Current score: {currentScore+1}")
    else:
        print(f"Sorry, that's wrong. Final Score: {finalScore}")   
'''
#Solution with guidance

def format_data (account):
    '''this function takes a random dictionary and formats its data'''
    accountName = account["name"]
    accountdesc = account["description"]
    accountCountr = account["country"]
    return(f"{accountName}, a {accountdesc}, from {accountCountr}")

def checkAnswer(guess, a_AccountFollowers, b_AccountFollowers):
    if a_AccountFollowers > b_AccountFollowers:
        return guess == "a"
    else:
        return guess =="b"

#Display art
print(logo)
score = 0
gameShouldContinue = True
#Generate a random account from the game data
import random
import os
randAccount_B = random.choice(data)
#Make the game repeatable
while gameShouldContinue:
    
    randAccount_A = randAccount_B
    randAccount_B = random.choice(data)
    while randAccount_A == randAccount_B:
        randAccount_B = random.choice(data)


    #Format account data into printable format
    accountA = format_data(randAccount_A)
    accountB = format_data(randAccount_B)

    print(f"Compare A: {accountA}")
    print(vs)
    print(f"Compare B: {accountB}")


    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct
    ##Get follower account of each account
    A_accout_followers = randAccount_A["follower_count"]
    B_accout_followers = randAccount_B["follower_count"]
    ##use if statement to check if user is correct

    is_Correct = checkAnswer(guess=guess, a_AccountFollowers=A_accout_followers, b_AccountFollowers=B_accout_followers)
    #Clear the screen
    os.system("cls")
    print(logo)

    #Give user feedback on their guess and #Score keeping
    if is_Correct:
        score+=1
        print(f"You are right! Current Score: {score}")
    else:
        gameShouldContinue = False
        print(f"You are wrong! Final Score: {score}")