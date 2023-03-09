import turtle
  
def moving_object(move):
    move.fillcolor('red') 
    move.begin_fill()
    move.circle(20)
    move.end_fill()

if __name__ == "__main__" :
    
    screen = turtle.Screen()
    screen.setup(992,540)
    screen.bgpic("tablepic.png")   

    screen.tracer(0)           

    move = turtle.Turtle() 
    move.color('red')
    move.speed(0) 
    move.width(2)     
    move.hideturtle()        
    move.penup()            
    move.goto(-250, 0) 
    move.pendown()             

    # infinite loop
    while True :
        move.clear()  
        moving_object(move)   
        screen.update()    
        move.forward(0.5)
    
    turtle.done()