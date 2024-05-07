import turtle

class Sun:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')

    def draw(self):
        for _ in range(36):
            self.t.forward(200)
            self.t.backward(200)
            self.t.right(10)

# Create an instance of Sun and draw it
sun = Sun()
sun.draw()

# Keep the window open until manually closed
turtle.mainloop()
