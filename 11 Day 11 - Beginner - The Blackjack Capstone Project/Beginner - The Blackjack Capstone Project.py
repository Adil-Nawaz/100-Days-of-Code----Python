from asciiart import logo
import random
import os
print(logo)

def dealCard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    getCard = random.choice(cards)
    return getCard

def calculateScore(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:   #used to see/look up a specific number inside list 11
        card.remove(11)
        card.append(1)
    return sum(card)
def compareScores(user, computer):
    if user == computer:
        return "Its draw"
    elif computer == 0:
        return "You lose: Computer has blackjack"
    elif user == 0:
        return "You win with a blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif computer > 21:
        return "Computer went over. You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"

userCards = []
computerCards = []
is_Game_over = False
# userCards.append(dealCard())
# userCards.append(dealCard())
for _ in range(2):
    userCards.append(dealCard())
    computerCards.append(dealCard())

while not is_Game_over:            
    userScore = calculateScore(userCards)
    print(f"Your cards are {userCards} and your score is {userScore}")
    # computerCards.append(dealCard())
    # computerCards.append(dealCard())
    computerScore = calculateScore(computerCards)
    print(f"Computer's first card is {computerCards[0]} ")
    if userScore == 0 or computerScore == 0 or userScore > 21:
        is_Game_over = True
    else:
        anotherCard = input("Do you want to draw another card? (y/n) ")
        if anotherCard == "y":
            userCards.append(dealCard())
        else:
            is_Game_over = True
while computerScore!=0 and computerScore <17:
    computerCards.append(dealCard())
    computerScore = calculateScore(computerCards)

print(f"Your final hand is: {userCards} and final score is: {userScore}")
print(f"Computer's final hand is: {computerCards} and its final score is: {computerScore}")
print(compareScores(user=userScore, computer=compareScores))

clrScr = input("Clear screen? (y/n)")
if clrScr=="y":
    os.system("cls")