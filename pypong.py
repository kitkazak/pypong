# A simple Pong game written in Python 3
# Original tutorial by youtube.com/@TokyoEdTech

import turtle

window = turtle.Screen()
window.title('PyPong')
window.bgcolor('#868188')
window.setup(width = 800, height = 600)

# Stops the window from updating,
# so that it needs to be manually updated
window.tracer(0)

# BG
bg_a = turtle.Turtle()
bg_a.speed(0)
bg_a.shape('square')
bg_a.color('#212123')
bg_a.shapesize(stretch_len = 40, stretch_wid = 30)
bg_a.penup()
bg_a.goto(0, 0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('#f2f0e5')
paddle_a.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('#f2f0e5')
paddle_b.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('#f2f0e5')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if (paddle_a.ycor() >= 260):
        y = 260
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if (paddle_a.ycor() <= -260):
        y = -260
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if (paddle_b.ycor() >= 260):
        y = 260
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if (paddle_b.ycor() <= -260):
        y = -260
    paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 340:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1

    if ball.xcor() < -340:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1

    # Paddle and ball collisions
    # Paddle A
    if ball.xcor() == -330 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1

    # Paddle B
    if ball.xcor() == 330 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1