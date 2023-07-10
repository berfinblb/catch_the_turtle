import turtle
import random
from random import randint
import time

# Screen settings
turtle_screen = turtle.Screen()
turtle_screen.title("Catch the turtle ")
turtle_screen.bgcolor("pink")

# top height and width
top_height = int(turtle_screen.window_height() / 2)
top_width = int(turtle_screen.window_width() / 2)
tur = turtle.Turtle()

# Shape of the turtle
tur.shape("turtle")
tur.shapesize(4, 4)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "orange", "SlateGray",
           "#AB82FF", "#9AFF9A"]

FONT = ("Arial", 30, "normal")
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
score = 0
game_over = False


def score_refresh():
    def handle(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    tur.onclick(handle)


# score
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("#FF4500")
    score_turtle.penup()
    score_turtle.goto(0, 260)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)


# turtle position
def move_turtle():
    if not game_over:
        for i in range(20):
            tur.penup()

            tur.setpos(randint(-top_width, top_height), randint(-top_height, top_width))
            tur.color(random.choice(colours))


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("#458B74")
    countdown_turtle.penup()

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 80)
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        turtle_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over! : {}".format(time), move=False, align="center", font=FONT)
        tur.hideturtle()


def start_game_up():
    score_refresh()
    countdown(10)
    setup_score_turtle()
    move_turtle()


start_game_up()

turtle.mainloop()
