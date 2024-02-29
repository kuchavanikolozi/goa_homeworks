from math import *
from turtle import *

#step 1 - drawing a square 

speed(15)
color("red")
width(7)

forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)

penup()
goto(160,160)
pendown()

begin_fill()
left(120)
forward(sqrt(71 * 71 + 142* 142)) 

left(120)
forward(sqrt(71 * 71 + 142 * 142))
end_fill()

penup()
goto(-200,0)
pendown()

left(120)
forward(160)
left(90)
forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)

penup()
goto(-40,160)
pendown()

begin_fill()
left(120)
forward(sqrt(71 * 71 + 142* 142)) 

left(120)
forward(sqrt(71 * 71 + 142 * 142))
end_fill()

penup()
goto(200,0)
pendown()


left(120)
forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)

forward(160)
left(90)

penup()
goto(360,160)
pendown()

begin_fill()
left(120)
forward(sqrt(71 * 71 + 142* 142)) 

left(120)
forward(sqrt(71 * 71 + 142 * 142))
end_fill()

penup()
goto(-800,400)
pendown()

#sun
begin_fill()
color("yellow")
circle(100)
end_fill()

#grass
penup()
goto(-800,-10)
pendown()
color("dark green")
left(120)
forward(290)
forward(290)
forward(290)
forward(290)
forward(290)
forward(290)

#tree
penup()
goto(-450,100)
pendown()

color("brown")
right(90)
forward(110)
penup()
goto(-400,0)
pendown()

forward(5)
right(180)
forward(105)

penup()
goto(-300,5)
pendown()

penup()
goto(-400,5)
pendown()

forward(90)

penup()
goto(-380,140)
pendown()

color("green")
begin_fill()
circle(50)
end_fill()







exitonclick()