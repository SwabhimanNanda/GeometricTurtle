import turtle

class Star:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(5):
            self.t.forward(100)
            self.t.right(144)

# Create an instance of Star and draw it
star = Star()
star.draw()

# Keep the window open until manually closed
turtle.mainloop()
