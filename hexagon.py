import turtle

class Hexagon:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(6):
            self.t.forward(100)
            self.t.left(60)

# Create an instance of Hexagon and draw it
hexagon = Hexagon()
hexagon.draw()

# Keep the window open until manually closed
turtle.mainloop()
