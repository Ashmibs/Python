"""
Program: Double arrow
Author: Ashmi Bidrupane Suresh
Description: The Recreation of double arrow using turtle
	00 - Announce and the pointer is moved to starting position
	01 - Found the length of the arrow head for the isoceles triangle 
	02 - To complete double arrow drawing and move pointer to the starting position.
"""
#access the turtle mode
import turtle
#establish the drawing window
canvas = turtle.Screen()
#assigning turtle variable
tom=turtle.Turtle()

#Announce
print("Double Arrow")

#Move the turtle to the position from where the double arrow creation needs to be started

#To move the pen without drawing on screen
tom.penup()
#To move the turtle pointer 90 degrees to the left
tom.left(90)
#To move the turtle in the direction of turtle poineter
tom.forward(50)

#To start drawing the double arrow

#To put the pen down so that the turtle draws along its movement
tom.pendown()
#To move the turtle pointer 90 degrees to the right
tom.right(90)
tom.forward(100)
tom.left(90)
tom.forward(50)

#The Arrow head is an isosceles triangle , the length of the triangle is calculated which is 141.4 
tom.right(135)
tom.forward(141.4)
tom.right(90)
tom.forward(141.4)
tom.right(135)
tom.forward(50)
tom.left(90)
tom.forward(200)
tom.left(90)
tom.forward(50)
tom.right(135)
tom.forward(141.4)
tom.right(90)
tom.forward(141.4)
tom.right(135)
tom.forward(50)
tom.left(90)
tom.forward(100)

#To move the turtle to the same starting position
tom.right(90)
tom.penup()
tom.forward(50)
tom.left(90)
