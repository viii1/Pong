import turtle # Small "T" cause its a modular name

#For windows
wn = turtle.Screen() # Here the origin is at the center of the screen unlike pygame or openCV
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800,height=600)

""" stop the windows from updating
 we have to update it manually 
 And it helps in speeding up the game """

wn.tracer(0)

score_a = 0
score_b = 0

#pen
pen=turtle.Turtle()
pen.speed(0) # animation speed
pen.color("white")
pen.penup() # dont wanna see the line between the points
pen.hideturtle()
pen.goto(0,270)
pen.write("Player A :0 Player B :0",align="center",font=("courier",24,"normal"))


#Paddle A
paddle_a = turtle.Turtle() # Capital "T" cause its the class name
paddle_a.speed(0) # this is the speed of animation not the sped of the paddle, it is set to the maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # turtle drawas a line when moving and we dont want this 
paddle_a.goto(-350,0)


#Padle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=3
ball.dy=3

#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    if paddle_a.ycor() <250:
        y+=20
        paddle_a.sety(y)
    else:
        paddle_a.sety(250)

def paddle_a_down():
    y=paddle_a.ycor()
    if paddle_a.ycor() >-250:
        y-=20
        paddle_a.sety(y)
    else:
        paddle_a.sety(-250)

def paddle_b_up():
    y=paddle_b.ycor()
    if paddle_b.ycor() <250:
        y+=20
        paddle_b.sety(y)
    else:
        paddle_b.sety(250)

def paddle_b_down():
    y=paddle_b.ycor()
    if paddle_b.ycor() >-250:
        y-=20
        paddle_b.sety(y)
    else:
        paddle_b.sety(-250)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") #Lowercase "w" will only work not the upper case
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



#Main game loop

while True:
    wn.update() #tap = 4 spaces keys use either not both otherwise you may face some error


    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A :{} Player B :{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))


    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A :{} Player B :{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))

    #Paddle and ball collision
    if ball.xcor()>340 and (ball.ycor() < (paddle_b.ycor()+ 50) and ball.ycor() > (paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor()<-340 and (ball.ycor() < (paddle_a.ycor()+ 50) and ball.ycor() > (paddle_a.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1


    


