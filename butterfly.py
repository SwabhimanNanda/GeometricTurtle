import turtle

class Butterfly:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(2):
            self.t.circle(50, 180)
            self.t.left(180)

# Create an instance of Butterfly and draw it
butterfly = Butterfly()
butterfly.draw()

# Keep the window open until manually closed
turtle.mainloop()
