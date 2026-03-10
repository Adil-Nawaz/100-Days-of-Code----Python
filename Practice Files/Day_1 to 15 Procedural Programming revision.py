#Day 1 no need
#Day 2 String Manipulation
#Adding a 2 digit number 
''' 
number = input("Enter a 2 digit number to add: ")
digit1 = int(number[0])
digit2 = int(number[1])
print(f"Sum of 2 digit number {number} is: {digit1+ digit2}") 



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
letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

generatedPass = []
random.shuffle(lettersList)
random.shuffle(numbersList)
random.shuffle(symbolsList)
for letter in range(0,letters):
    generatedPass.append(lettersList[letter])
for symbol in range(0,symbols):
    generatedPass.append(symbolsList[symbol])
for number in range(0, numbers):
    generatedPass.append(numbersList[number])
random.shuffle(generatedPass)
finalPass = ""

print(finalPass.join(generatedPass))

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_Bank = []

for question in question_data:
    questionText = question["text"]
    questionAnswer = question["answer"]
    newquestion = Question(q_text=questionText, q_answer=questionAnswer)
    question_Bank.append(newquestion)

quiz = QuizBrain(q_list=question_Bank)
while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("Congratulations! You have completed all questions")
print(f"Your final score is: {quiz.score} / {len(question_Bank)}")
'''

# from turtle import Turtle, Screen
# import random
# endOfgame = False
# colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# screen = Screen()
# screen.setup(width=500, height=400)
# ypos = -100
# turtlesList = []
# userChoice = screen.textinput(title="Which turtle is going to win? ", prompt="Enter the color of turtle: ")
# for turtles in range(0, len(colors)):
#     tim = Turtle(shape="turtle")
#     tim.penup()
#     tim.color(colors[turtles])
#     tim.goto(-230,ypos)
#     ypos += 40
#     turtlesList.append(tim)

# if userChoice:
#     endOfgame = True

# while endOfgame:
#     for i in turtlesList:
#         if i.xcor() > 230:
#             endOfgame = False
#             if i.pencolor() == userChoice:
#                 print(f"You have won {i.pencolor()} turtle has won")
#             else:
#                 print(f"You have lost {i.pencolor()} turtle has won")
#         randDist = random.randint(0,10)
#         i.forward(randDist)
#screen.exitonclick()

