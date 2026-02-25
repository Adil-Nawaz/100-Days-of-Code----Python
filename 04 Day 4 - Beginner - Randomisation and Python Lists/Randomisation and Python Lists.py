import random
print(random.random())
random_integer =  random.randint(1, 20)
print(random_integer)

#Heads or Tails of Coin
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

#Lists
fruits = ["apples", "bananana","lemon"]
for i in range(0,3):
    print(fruits[i])
fruits[1] = "Banana"
for i in range(0,3):
    print(fruits[i])
fruits.append("Watermelon")
for i in range(0,4):
    print(fruits[i])
fruits.extend(["Mango", "Grapes", "Guava"])
for i in range(0,7):
    print(fruits[i])

#Who will pay the bill 1.0
#Sample data for input Zayan, Areeba, Hamza, Elina, Farhan, Mehwish, Danish, Hira, Saad, Alina
import random
participants = input("Enter the names of all participants separating each name with comma ',': ")
names_list = participants.split(", ")
randomPerson = random.randint(0,len(names_list)-1)
print(f"The person who is paying the bill today is: {names_list[randomPerson]}")

#Who will pay the bill 1.1
import random
participants = input("Enter the names of all participants separating each name with comma ',': ")
names_list = participants.split(", ")
print(f"The person who is paying the bill today is: {random.choice(names_list)}")

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
                     "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", 
                     "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
                     "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", 
                     "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
                     "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
                     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", 
                     "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
                     ] 
print(len(states_of_america))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[0][0])
print(dirty_dozen[0][1])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
print(dirty_dozen[1][1])

#Treasure Map
row1 = ["🤣","😝","😊"]    #["🤣","😝","😊"] ["🤨","😗","😡"] ["😟","😣","🥺"]
row2 = ["🤨","😗","😡"]       # 0                    1               2
row3 = ["😟","😣","🥺"]
map = [row1, row2, row3] #0,1,2
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_Row = map[vertical-1]
selected_Row[horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

#Exercise 4
# Rules to follow:
# Rock beats Scissors (rock crushes scissors)
# Scissors beats Paper (scissors cut paper)
# Paper beats Rock (paper covers rock)

print("******** WELCOME TO THE ROCK PAPER SCIZZOR PROGRAM ********")
import random
Rock = '''
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    PAPER
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    SCISSORS
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    user_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    options = [Rock, Paper, Scissors]
    if user_Choice >= 3 or user_Choice < 0:
        print("Invalid Choice. Try Again!")
        continue
    
    print(f"You chose \n {options[user_Choice]}")
    pc_Choice = random.randint(0,2)
    print(f"PC chose \n {options[pc_Choice]}")

    if user_Choice == pc_Choice:
        print(f"Its a draw!")
    elif(
        ( user_Choice == 0 and pc_Choice == 2) or
        ( user_Choice == 1 and pc_Choice == 0) or
        ( user_Choice == 2 and pc_Choice == 1)
    ):
        print(" You Win ")
    else:
        print(" You Lose..!")

    playagain = input("Want to play again? (y/n) ").lower()
    if playagain == "y":
        continue
    else:
        break

print("******** THIS IS THE END OF THE PROGRAM PROGRAM ********")
