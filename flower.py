import turtle

class Flower:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(36):
            self.t.forward(100)
            self.t.right(170)

# Create an instance of Flower and draw it
flower = Flower()
flower.draw()

# Keep the window open until manually closed
turtle.mainloop()
