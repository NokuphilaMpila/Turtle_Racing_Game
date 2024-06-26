import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['purple', 'blue', 'green', 'orange', 'brown' 'red', 'yellow', 'black', 'pink', 'cyan']

def get_number_of_turtles():
    turtles = 0
    while True:
        turtles = input("Enter the number of turtles (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("Input is not valid...Try again!")
            continue

        if 2<= turtles <= 10:            
          return turtles
        else:
            print("Number not in range 2-10.Try again")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for turtle in turtles:
            distance = random.randrange(1, 20)
            turtle.forward(distance)

            x, y = turtle.pos()
            if y >= HEIGHT // 2 - 10:
                return color[turtles.index(turtle)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        turtles = turtle.Turtle()       
        turtle.color(color)
        turtle.shape('turtle')
        turtle.left(90)
        turtle.penup()
        turtle.setpos(-WIDTH //2 + (i +1) * spacingx, -HEIGHT//2 + 20)
        turtle.pendown()
        turtles.append(turtle)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game!")

turtles = get_number_of_turtles()
init_turtle()random.shuffle(COLORS)
colors = COLORS[:turtles]

winner = race(colors)
print("The winner is turtle color:", winner)
time.sleep(5)


      

          
