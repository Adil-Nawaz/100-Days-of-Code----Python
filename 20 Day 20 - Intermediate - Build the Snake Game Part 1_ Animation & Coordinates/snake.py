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


    def createSnake(self):
        for dots in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            snake.goto(self.xpos,0)
            self.xpos -= 20
            self.snakeDots.append(snake)


    def move(self):
        for segments in range(len(self.snakeDots)-1,0,-1):
            new_x = self.snakeDots[segments-1].xcor()
            new_y = self.snakeDots[segments-1].ycor()
            self.snakeDots[segments].goto(new_x, new_y)
        self.snakeDots[0].forward(20)


    def moveUp(self):
        if self.snakeDots[0].heading() != DOWN:
            self.snakeDots[0].setheading(UP)
    def movedown(self):
        if self.snakeDots[0].heading() != UP:
           self.snakeDots[0].setheading(DOWN)
    def moveleft(self):
        if self.snakeDots[0].heading() != RIGHT:
           self.snakeDots[0].setheading(LEFT)
    def moveright(self):
        if self.snakeDots[0].heading() != LEFT:
            self.snakeDots[0].setheading(RIGHT)
