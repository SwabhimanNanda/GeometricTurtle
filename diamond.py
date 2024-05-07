import turtle

class Diamond:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(2):
            self.t.forward(100)
            self.t.right(60)
            self.t.forward(100)
            self.t.right(120)

# Create an instance of Diamond and draw it
diamond = Diamond()
diamond.draw()

# Keep the window open until manually closed
turtle.mainloop()
