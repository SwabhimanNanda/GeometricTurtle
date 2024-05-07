import turtle

class Spiral:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for i in range(100):
            self.t.forward(i)
            self.t.right(45)

# Create an instance of Spiral and draw it
spiral = Spiral()
spiral.draw()

# Keep the window open until manually closed
turtle.mainloop()
