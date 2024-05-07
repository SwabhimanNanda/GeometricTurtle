import turtle

class Pentagon:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(5):
            self.t.forward(100)
            self.t.left(72)

# Create an instance of Pentagon and draw it
pentagon = Pentagon()
pentagon.draw()

# Keep the window open until manually closed
turtle.mainloop()
