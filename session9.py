from turtle import *

pencolor("red")
shape("turtle")
pensize(8)

shekls=["cirlcle","square","rectangle","triangle"]
print(shekls)

user=input("select a shape of top list:")
if user == "circle":
    circle(100)
    done()