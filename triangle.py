import turtle

class Triangle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(3):
            self.t.forward(100)
            self.t.left(120)

# Create an instance of Triangle and draw it
triangle = Triangle()
triangle.draw()

# Keep the window open until manually closed
turtle.mainloop()
