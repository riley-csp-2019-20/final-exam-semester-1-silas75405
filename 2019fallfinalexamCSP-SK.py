#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Silas Kubicki
#Date
# 12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
draw = trtl.Turtle()
draw.speed(0)

#variables
size = 1

#movement functions
def Up():
    draw.setheading(90)
    draw.forward(5)

def Down():
    draw.setheading(270)
    draw.forward(5)

def Right():
    draw.setheading(0)
    draw.forward(5)

def Left():
    draw.setheading(180)
    draw.forward(5)    


#color/drawing functions

#clear funtion
def clear():
    draw.reset()

#pensize funtions
def penBig():
    draw.pensize(size)

def sizeUp():
    global size
    size += 1

def penSmall():
    draw.pensize(size)

def sizeDown():
    global size
    size = size - 1

#penup functions
def pickUp():
    draw.penup()

def putDown():
    draw.pendown()

#color change
def Blue():
    draw.pencolor("Blue")

def Red():
    draw.pencolor("Red")

def Yellow():
    draw.pencolor("Yellow")

def Green():
    draw.pencolor("Green")


if (pickUp):
    putDown()
else:
    pickUp()

#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(clear, "space")
wn.onkeypress(penBig, "o")
wn.onkeyrelease(sizeUp, "o")
wn.onkeypress(penSmall, "p")
wn.onkeyrelease(sizeDown, "p")
wn.onkeypress(pickUp, "u")



#keys for color change
wn.onkeypress(Blue, "b")
wn.onkeypress(Red, "r")
wn.onkeypress(Yellow, "y")
wn.onkeypress(Green, "g")
#listen
wn.listen()

#mainloop
wn.mainloop()