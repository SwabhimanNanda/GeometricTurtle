import turtle

class Octagon:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(8):
            self.t.forward(100)
            self.t.left(45)

# Create an instance of Octagon and draw it
octagon = Octagon()
octagon.draw()

# Keep the window open until manually closed
turtle.mainloop()
