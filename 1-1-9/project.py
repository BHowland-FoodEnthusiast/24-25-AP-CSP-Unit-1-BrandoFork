import turtle as trtl
global xpos, ypos
import random as rd
# initialize turtle to begin painting
def init():
    global xpos, ypos
    xpos = 250
    ypos = 300
    clouds.speed(0)


clouds = trtl.Turtle()
clouds.penup()



init()
clouds.circle(360, 360, 360)
# making and coloring clouds
def cloud_draw():
    global xpos, ypos
    for cloud in range(3):
        if cloud % 2 == 0:
            ypos -= 20
            xpos -= 50

        else:
            ypos += 20
            xpos -= 50
        clouds.penup()
        clouds.goto(xpos, ypos)
        clouds.pendown()
        clouds.fillcolor('grey')
        clouds.begin_fill()
        clouds.circle(50)
        clouds.end_fill()
        # move pen to make next cloud
        clouds.penup()
        clouds.pendown()
for cloud in range(2):
    xpos -= 150
    ypos = 300
    cloud_draw()
#painting the ground
def grass_draw():
    global xpos, ypos
    xpos = -470
    ypos = -400
    clouds.penup()
    clouds.goto(xpos, ypos)
    clouds.pendown()
    clouds.left(90)
grass_draw()
clouds.color('#038c25')
for range in range(700):
    clouds.forward(rd.randint(50, 100))
    xpos += 2
    clouds.pendown()
    clouds.goto(xpos, ypos)
    clouds.penup()



wn = trtl.Screen()
wn = trtl.Screen()
#painting the sky
wn.bgcolor('#B2BEB5')
wn.mainloop()