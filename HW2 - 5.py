# Your name: Kushal Sanjeev
# Your student id: 46299632
# Your email: kasanj@umich.edu
# List who you worked with on this homework:

# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_scene(turtle):
    bgcolor("orange")
    turtle.penup()
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)

    turtle.pendown()
    def ghostbody(size):
        turtle.fillcolor("white")
        turtle.pencolor("white")
        turtle.begin_fill()
        for i in range(4):
            turtle.left(90)
            turtle.forward(size)
        turtle.end_fill()
    ghostbody(200)

    turtle.penup()
    turtle.left(90)
    turtle.forward(200)

    def ghosthead(num):
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(num)
        turtle.end_fill()
    ghosthead(100)

    turtle.right(180)
    turtle.forward(200)
    turtle.right(90)

        
    def ghostbot(number):
        turtle.fillcolor("white")
        turtle.begin_fill()
        for i in range(number):
            turtle.forward(20)
            for i in range(3):
                turtle.left(120)
                turtle.forward(20)
        turtle.end_fill()
    ghostbot(10)

    turtle.penup()
    turtle.goto(-30, 50)
    turtle.pendown()

    def ghosteyes(numbe):
        turtle.fillcolor("orange")
        turtle.begin_fill()
        for i in range(numbe):
            turtle.forward(40)
            for i in range(3):
                turtle.left(120)
                turtle.forward(40)
        turtle.end_fill()
    ghosteyes(1)

    turtle.penup()
    turtle.goto(30, 50)
    turtle.pendown()
    
    ghosteyes(1)

    turtle.penup()
    turtle.goto(-25, -50)
    turtle.pendown()

    def ghostmouth(num):
        turtle.fillcolor("orange")
        turtle.begin_fill()
        turtle.circle(num)
        turtle.end_fill()
    ghostmouth(12)

    turtle.penup()
    turtle.goto(200, -200)
    turtle.setheading(0)
    turtle.pendown()

    def initials(nu):
        for i in range(nu):
            turtle.pencolor("black")
            turtle.right(90)
            turtle.forward(50)
            turtle.right(180)
            turtle.forward(25)
            turtle.right(150)
            turtle.forward(33)
            turtle.right(180)
            turtle.forward(33)
            turtle.setheading(0)
            turtle.left(60)
            turtle.forward(33)
            
            turtle.penup()
            turtle.goto(200, -200)
            turtle.setheading(0)
            turtle.forward(50)

            turtle.pendown()
            turtle.left(180)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(30)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(30)

    initials(1)

def main():
    place = Screen()
    carlos = Turtle()
    draw_scene(carlos)
    place.exitonclick()

    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
