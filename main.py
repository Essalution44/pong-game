import turtle
wn = turtle.Screen()
wn.title("Essalution44")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score1 = 0
score2 = 0

# player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x_speed = 2
ball.y_speed = 2

# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("player 1: 0     player 2: 0", align="center", font=("Courier", 24, "normal"))


# functions


def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)
# keyboard binding


wn.listen()
wn.onkeypress(player1_up, "w")
wn.onkeypress(player1_down, "s")
wn.onkeypress(player2_up, "Up")
wn.onkeypress(player2_down, "Down")
# main game

while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor()+ball.x_speed/4)
    ball.sety(ball.ycor()+ball.y_speed/4)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.y_speed *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.y_speed *= -1
    elif ball.xcor() > 350:
        score1 += 1
        pen.clear()
        pen.write("player 1: {}    player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.x_speed *= -1
    if ball.xcor() < -290:
        score2 += 1
        pen.clear()
        pen.write("player 1: {}     player 2: {}".format(score1, score2), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.x_speed *= -1
    if ball.xcor() < -340 and ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50:
        ball.x_speed *= -1
    elif ball.xcor() > 340 and ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50:
        ball.x_speed *= -1


#   MADE BE ESSALUTION44
