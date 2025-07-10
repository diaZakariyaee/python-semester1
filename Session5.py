from turtle import *

fillcolor("black")
begin_fill()

circle(100,180)
left(180)
circle(-50,180)
circle(50,180)

end_fill()

left(180)
circle(-100,180)

backward(10)
right(90)
penup()
forward(50)
pendown()

fillcolor("black")
begin_fill()
circle(15)
end_fill()

penup()
forward(100)
pendown()

fillcolor("white")
begin_fill()
circle(15)
end_fill()

done()