import turtle

def UP():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

turtle.onkey(UP,'w')

    
def LEFT():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
turtle.onkey(LEFT,'a')

def RIGHT():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
turtle.onkey(RIGHT,'d')

def DOWN():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
turtle.onkey(DOWN,'s')
    
def restart():
    turtle.reset()
  

turtle.shape('turtle')

turtle.onkey(restart,'Escape')
turtle.listen()
