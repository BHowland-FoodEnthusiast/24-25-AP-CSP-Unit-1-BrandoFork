import turtle as trtl
global xpos, ypos
import random as rd
# initialize turtle to begin painting
def init():
    global xpos, ypos
    xpos = 480
    ypos = 300
    clouds.speed(0)
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

        clouds.penup()
        clouds.pendown()


clouds = trtl.Turtle()
clouds.penup()
init()


# making and coloring clouds

#making three clouds
for cloud in range(3):
    xpos -= 150
    ypos = 300
    cloud_draw()

#method for painting the grass
def grass_draw():
    global xpos, ypos
    xpos = -500
    ypos = -400
    clouds.penup()
    clouds.goto(xpos, ypos)
    clouds.pendown()
    clouds.left(90)

#paints the grass
grass_draw()
clouds.color('#038c25')
for range in range(1000):
    clouds.forward(rd.randint(50, 100))
    xpos += 1
    clouds.pendown()
    clouds.goto(xpos, ypos)
    clouds.penup()





wn = trtl.Screen()
#painting the sky
wn.bgcolor('#B2BEB5')
wn.mainloop()