print("---PONG---")

import time
from pongScreen import PongScreen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

pongScreen = PongScreen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pongScreen.setupInput(r_paddle, l_paddle)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    pongScreen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 and ball.xcor() < 330 or ball.distance(l_paddle) < 70 and ball.xcor() < -320 and ball.xcor() > -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

PongScreen.screen.exitonclick()
