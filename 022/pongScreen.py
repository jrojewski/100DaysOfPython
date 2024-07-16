from turtle import Screen

HEIGHT = 600
WIDTH = 800

class PongScreen():
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.screen.listen()

    def setupInput(self, r_paddle, l_paddle):
        self.screen.onkeypress(r_paddle.go_up, "Up")
        self.screen.onkeypress(r_paddle.go_down, "Down")
        self.screen.onkeypress(l_paddle.go_up, "w")
        self.screen.onkeypress(l_paddle.go_down, "s")

    def update(self):
        self.screen.update()
