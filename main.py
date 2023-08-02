#Turtle Party 07/31/23
#print("Challenge #",2+3)
#import turtle

#turtle.color("blue")
#distance = 50
#turtle.forward(distance)
#turtle.left(120)
#turtle.forward(distance)
#turtle.left(120)
#turtle.forward(distance)
#turtle.left(120)

#turtle.color("blue")
#distance = 50
#repeat  3 times
#for sides in range(3):
#  turtle.forward(distance)
#  turtle.left(120)
import turtle
turtle.color("blue")

def polygon(size,sides):
  for i in range(sides):
    turtle.forward(size)
    turtle.left(360/sides)
 
def polyloop(size):
  for i in range(3,13):
    turtle.color(i*20,i*10,250-i*10)
    polygon(size/i,i)
    move(size/2,36)
    
    
def back(dist):
  turtle.penup()
  turtle.back(dist)
  turtle.pendown()

def forward(dist):
  turtle.penup()
  turtle.forward(dist)
  turtle.pendown()
  
def move(dist,dir):
  turtle.penup()
  turtle.left(dir)
  turtle.forward(dist)
  turtle.pendown()
  
def spiral(length,angle,lenchange,turns):
  for i in range(turns):
    turtle.forward(length+i*lenchange)
    turtle.left(angle)
    
  

polyloop(100)
turtle.color("blue")
move(100,180)
spiral(4,90,5,20)
move(180,0)
turtle.color("green")
spiral(5,45,5,13)

#polygon(50,3)
#back(75)
#polygon(75,4)
#polygon(100,2)
