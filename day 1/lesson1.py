from turtle import *


#we want to paint a house
#step 1:   draw a square
speed(20)
width(7)
color("brown")          
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120)     #height of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60,140)    #sizes
pendown()
right(150)
color("blue")
begin_fill()
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)
end_fill()

penup()
goto(140,140)
pendown()
color("blue")
begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()



exitonclick()




























print("luka gogokhia")

print(5)           #integer            int
print("5")         #string      #str

print(5 + int("5"))

#qweqweqweqwe
print("luka gogokhia aris " + "5" + " wlis")