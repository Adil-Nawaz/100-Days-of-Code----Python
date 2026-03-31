from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakeDots = []
        self.xpos = 0 
        self.createSnake()
        self.head = self.snakeDots[0]


    def createSnake(self):
        for dots in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            snake.goto(self.xpos,0)
            self.xpos -= 20
            self.snakeDots.append(snake)

#This code is mind blowing understand it in lecture 184 to know the concept of moving objects
    def move(self):
        for segments in range(len(self.snakeDots)-1,0,-1):
            new_x = self.snakeDots[segments-1].xcor()
            new_y = self.snakeDots[segments-1].ycor()
            self.snakeDots[segments].goto(new_x, new_y)
             #till this code all segments will be placed at one place because we are not moving the first segment fwd
        self.snakeDots[0].forward(20) #this code will fwd first segment forward and above code will change the positions of other blocks

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def movedown(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)
    def moveleft(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
    def moveright(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
