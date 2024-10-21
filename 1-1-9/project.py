import turtle as trtl

# move pen to start making clouds
clouds = trtl.Turtle()
clouds.penup()
global xpos, ypos
xpos = 250
ypos = 300
clouds.bgcolor = 'gray'
# making and coloring clouds
def cloud_draw():
    global xpos, ypos
    for cloud in range(15):
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

cloud_draw()
wn = trtl.Screen()
wn.mainloop()