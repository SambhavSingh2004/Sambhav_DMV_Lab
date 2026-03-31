import turtle
import time

screen = turtle.Screen()
screen.title("Bouncing Ball")
screen.bgcolor("white")
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)

dx = 3
dy = 2

while True:
    screen.update()
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if ball.xcor() > 290 or ball.xcor() < -290:
        dx *= -1
    if ball.ycor() > 290 or ball.ycor() < -290:
        dy *= -1
    
    time.sleep(0.01)