import turtle

class Arrow:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        self.t.left(90)
        self.t.forward(100)
        self.t.right(135)
        self.t.forward(50)
        self.t.backward(50)
        self.t.right(90)
        self.t.forward(50)
        self.t.backward(50)
        self.t.left(45)
        self.t.backward(100)

# Create an instance of Arrow and draw it
arrow = Arrow()
arrow.draw()

# Keep the window open until manually closed
turtle.mainloop()
