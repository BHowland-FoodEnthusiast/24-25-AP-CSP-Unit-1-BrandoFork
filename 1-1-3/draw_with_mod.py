#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
color="blue"

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    if floor % 3 == 0:
        if color == "blue":
            color = "gray"
        else:
            color = "blue"
        painter.penup()
    painter.goto(x, y)
    painter.color(color)
    y = y + 5  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()