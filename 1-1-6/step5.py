#   a116_buggy_image.py
import turtle as trtl
# initialize turtle
spider = trtl.Turtle()
spider.pensize(40)
#draw the body

spider.circle(20)

#configures legs
num_legs = 8
leg_size = 70
iterations = 0
leg_rotation = 360 / num_legs
spider.pensize(5)


#draw the legs
while iterations < num_legs:
  spider.goto(0, 20)
  spider.setheading(leg_rotation * iterations)
  spider.forward(leg_size)
  iterations = iterations + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()