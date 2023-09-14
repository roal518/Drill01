import turtle

def move_left():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def restart():
    turtle.reset()
turtle.shape('turtle')
turtle.onkey(move_left,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
