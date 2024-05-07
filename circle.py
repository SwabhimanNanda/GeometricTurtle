import turtle

class Circle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        self.t.circle(100)

# Create an instance of Circle and draw it
circle = Circle()
circle.draw()

# Keep the window open until manually closed
turtle.mainloop()
