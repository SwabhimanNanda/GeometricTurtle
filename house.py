import turtle

class House:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(45)
        self.t.forward(70)
        self.t.left(90)
        self.t.forward(70)

# Create an instance of House and draw it
house = House()
house.draw()

# Keep the window open until manually closed
turtle.mainloop()
