import turtle

class Snowflake:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(6):
            self.branch()
            self.t.right(60)

    def branch(self):
        for _ in range(3):
            self.t.forward(30)
            self.t.backward(30)
            self.t.right(45)
        self.t.left(90)
        for _ in range(3):
            self.t.forward(30)
            self.t.backward(30)
            self.t.left(45)
        self.t.right(30)

# Create an instance of Snowflake and draw it
snowflake = Snowflake()
snowflake.draw()

# Keep the window open until manually closed
turtle.mainloop()
