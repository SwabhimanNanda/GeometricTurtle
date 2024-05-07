import turtle

class Heart:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        self.t.begin_fill()
        self.t.fillcolor('red')
        self.t.left(140)
        self.t.forward(224)
        self.t.circle(-90, 200)
        self.t.setheading(60)
        self.t.circle(-90, 200)
        self.t.forward(224)
        self.t.end_fill()

# Create an instance of Heart and draw it
heart = Heart()
heart.draw()

# Keep the window open until manually closed
turtle.mainloop()
