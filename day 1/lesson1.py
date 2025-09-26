from turtle import*


#we want to paint a house

#step 1: draw a square


speed(30)
color("coral")
begin_fill()
width(7)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
end_fill()
#end of squeare

#step 2: door

forward(70)
begin_fill()
color("brown")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# window 1
begin_fill()
color("blue")

left(30)
forward(80)
color("blue")
left(90)
forward(65)
left(90)
forward(80)
left(90)
end_fill()

#window 2

color("blue")
penup()
goto(200, 200)
pendown()

begin_fill()
left(90)
forward(80)
color("blue")
right(90)
forward(70)
right(90)
forward(80)
end_fill()











exitonclick()

