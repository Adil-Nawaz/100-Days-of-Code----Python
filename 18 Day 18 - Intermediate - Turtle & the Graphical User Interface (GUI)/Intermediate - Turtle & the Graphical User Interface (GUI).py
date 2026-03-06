
'''
#import turtle
#turtle.colormode(255)
from turtle import Turtle, Screen

#import turtle  #Second way


def drawSquare(name, steps):
    for _ in range(0,4):
        name.forward(steps)
        name.right(90)

def dashedLine(name,steps):
    for _ in range(10):
        name.pd()
        name.forward(steps)
        name.pu()
        name.forward(steps)

#timmy = turtle.Turtle()  #Second way
tim = Turtle()   #One way
tim.shape("turtle")
tim.color("blue")


#Draw a square challenge
drawSquare(tim,100)

#draw a dashed line challenge
tim.left(45)
tim.pu()
tim.forward(50)
dashedLine(tim,10)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 255, 255), 
          (255, 192, 203), (75, 0, 130), (60, 179, 113)]

def shapeBuilder(object, numberOfCorners):
    for _ in range(numberOfCorners):
        object.forward(100)
        object.right(360/numberOfCorners)

#Drawing geometrical shapes
tim2 = Turtle()
tim2.shape("turtle")
tim2.color(255,100,50)
colorNo = 0
for _ in range(3, 11):
    tim2.color(colors[colorNo])
    colorNo+=1
    shapeBuilder(tim2, _)
'''
#Beginner method
'''
for _ in range(3):
    tim2.forward(100)
    tim2.right(120)
for _ in range(4):
    tim2.forward(100)
    tim2.right(90)
for _ in range(5):
    tim2.forward(100)
    tim2.right(72)
for _ in range(6):
    tim2.forward(100)
    tim2.right(60)
for _ in range(7):
    tim2.forward(100)
    tim2.right(51.42)
for _ in range(8):
    tim2.forward(100)
    tim2.right(45)
for _ in range(9):
    tim2.forward(100)
    tim2.right(40)


#Random walk challenge one way
import random
colors = [
"red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
"black", "white", "gray", "cyan", "magenta", "gold", "silver",
"navy", "teal", "lime", "maroon", "violet"
]
tim3 = Turtle()
tim3.shape("turtle")
tim3.pensize(20)
tim3.speed(10)
for _ in range(0,50):
    tim3.color(random.choice(colors))
    randomFwd = tim3.forward(int(random.random()*50))
    randomLeft = tim3.left(random.randint(1,9)*40)
    tim3.color(random.choice(colors))
    randomFwd = tim3.forward(int(random.random()*50))
   # randomRight = tim3.right(random.randint(1,9)*40)
    randomLeft = tim3.left(random.randint(1,9)*40)


#Random walk challenge 2nd way
import turtle
turtle.colormode(255)
import random
def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

colors = [
"red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
"black", "white", "gray", "cyan", "magenta", "gold", "silver",
"navy", "teal", "lime", "maroon", "violet"
]
directions = [0, 90, 180, 270]

tim4 = Turtle()
tim4.shape("turtle")
tim4.pensize(20)
tim4.speed(0)
for _ in range(200):
    # tim4.color(random.choice(colors))
    # tim4.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim4.color(randomColor())
    tim4.forward(30)
    tim4.setheading(random.choice(directions))


#Method one but it will not stop until loop ends
import turtle as t
from turtle import Screen
import random
t.colormode(255)
t.speed(0)
def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

heading = 0.0
for _ in range(0,100):
    t.color(randomColor())
    t.circle(60)
    heading += 10
    t.setheading(heading)

#Method 2 which stops soon after making spirograph
import turtle as t
from turtle import Screen
import random
t.colormode(255)
t.speed(0)
def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_Spiro(size):
    for _ in range(int(360/size)):
        t.color(randomColor())
        t.circle(100)
        t.setheading(t.heading()+size)


draw_Spiro(5)

'''


import turtle as t
from turtle import Screen
import random
import colorgram
t.colormode(255)

colorsList = [(245, 238, 243), (246, 244, 242), (202, 110, 164), (240, 241, 245), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), 
              (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), 
              (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), 
              (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]
'''
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    red = color.rgb.r
    blue = color.rgb.b
    green = color.rgb.g
    newColor = (red,blue,green)
    colorsList.append(newColor)
print(colorsList)
'''


def makeDots(object,dotsize, distBtwDots):
    object.dot(dotsize,random.choice(colorsList))
    object.pu()
    object.forward(distBtwDots)
yPos = -212.13
tim1 = t.Turtle()
tim1.hideturtle()
# tim1.setheading(225)
tim1.pu()
# tim1.forward(300)
# tim1.setheading(0)
# print(tim1.pos())

tim1.goto(-212.13,-212.13)
for _ in range(0,10):
    for dots in range(0,10): 
        makeDots(tim1,20,50)
    yPos += 50
    tim1.goto(-212.13,yPos)
    






screen = Screen()
screen.exitonclick()