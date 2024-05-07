import turtle

class Square:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(4):
            self.t.forward(100)
            self.t.right(90)

# Create an instance of Square and draw it
square = Square()
square.draw()

# Keep the window open until manually closed
turtle.mainloop()
