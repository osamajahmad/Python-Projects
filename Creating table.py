""" This program uses Turtle graphics to draw a table and a cake. It lets the user customize the table's length, width, and color, 
as well as the cake's size. The program checks that the input values are within valid ranges.

Functions:
    front_legs(leg_length) - Draws the front legs of the table.
    right_legs(l, w, leg_length) - Draws the right side legs of the table.
    left_legs(l, w, leg_length) - Draws the left side legs of the table.
    top_table(l, w, color) - Draws the table's surface along with the legs and adds colour.
    cake_bot(a, b) - Draws the bottom layer of the cake.
    cake_middle(x, y) - Draws the middle layer of the cake.
    cake_top(p, q) - Draws the top layer of the cake.
    draw_candle() - Draws a candle on the cake.
    draw_star(size) - Draws a star.
    add_stars_to_layers() - Adds stars to each cake layer.
    main() - Runs the cake drawing functions.

User inputs:
    l - Length of the table (300-450).
    w - Width of the table (100-200).
    color - Color of the table.
    len_cake - Length of the cake (60-70).
    wid_cake - Width of the cake (30-40).

The program checks the input ranges before drawing the table and cake. """

"""Importing turtle to use trutle commands"""
import turtle

"""Defining function to draw front legs of table"""
def front_legs(leg_length):                      #leg_length is a variable that holds the 
    turtle.forward(leg_length)                   #dimensions of the table's legs.
    turtle.setheading(180)
    turtle.forward(30)                           #Standard width of the leg
    turtle.setheading(90)
    turtle.forward(leg_length)
    

"""Defining function to draw the legs of the table on the right side"""
def right_legs(l,w,leg_length):                 #Parameters include length,width and length of the leg
    front_legs(leg_length)                      #Calling function to draw the front leg
    turtle.left(90)
    turtle.penup()                              #Drawing back leg of the table
    turtle.forward(0.5*w)                       #Specifying space between the 2 legs on right side
    turtle.left(90)
    turtle.pendown()
    turtle.forward(leg_length-50)               #Back leg has to appear smaller than the front leg
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(leg_length-50)
    turtle.right(90)
    turtle.penup()
    turtle.goto(l/2,-100)
    turtle.left(180)


"""Defining function to draw the legs of the table on the left side"""
def left_legs(l,w,leg_length):                 #Parameters include length,width and length of the leg
    turtle.forward(l-30)                       #Turtle has moved to left side of the table, leaving 30
    turtle.setheading(270)                     # pixel space for the leg to be drawn
    turtle.pendown()
    front_legs(leg_length)                     #Calling function to draw the front leg
    turtle.penup()                             #Drawing back leg of the table
    turtle.setheading(180)                   
    turtle.right(60)                           #Going to starting point of back leg
    turtle.forward(w)
    turtle.pendown()
    turtle.left(150)
    turtle.forward(leg_length)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(leg_length)
    turtle.penup()
    

"""Defining function to draw the surface/top of the table"""
def top_table(l,w,color):                    #Parameters include length,width and colour of the entire table
    turtle.penup()
    turtle.pencolor(color)                   #Specifying the colour of the pen (through user input)
    turtle.pensize(5)                        #Specifying pen size
    turtle.fillcolor(color)                  #Specifying colour for the table top (through user input)
    turtle.begin_fill()
    turtle.goto(l/2,-100)                    #Going to starting point of drawing the table
    turtle.left(120)
    turtle.pendown()
    turtle.forward(w)
    turtle.left(60)
    turtle.forward(l)
    turtle.left(120)
    turtle.forward(w)
    turtle.left(60)
    turtle.forward(l)
    turtle.setheading(270)
    turtle.end_fill()
    turtle.begin_fill()                     #Specifying the colour of the legs of the table
    right_legs(l,w,leg_length)
    left_legs(l,w,leg_length)
    turtle.end_fill()
    turtle.home()                           #Returning turtle to original position    

"""Code for bottom layer of the cake"""
def cake_bot(a, b):
    turtle.penup()                      
    turtle.forward(a/2)                     #To ensure the layer is centered
    turtle.setheading(90)   
    turtle.forward(b)                       #Moving to where the bottom layer starts
    turtle.down()  
    turtle.setheading(360)  
    turtle.fillcolor("SaddleBrown") 
    turtle.begin_fill()              
    turtle.color("SaddleBrown")        
    turtle.forward(a/2)  
    turtle.setheading(270)  
    turtle.forward(b)                       #Move the turtle up to the height of the layer
    turtle.setheading(180)  
    turtle.forward(a) 
    turtle.setheading(90)  
    turtle.forward(b) 
    turtle.setheading(360) 
    turtle.forward(a/2)                    #Moving back to the center
    turtle.end_fill() 
    turtle.setheading(90)                  #Face up for the next layer
    

"""Code for middle layer of the cake"""
def cake_middle(x, y):
    turtle.up()
    turtle.forward(y) 
    turtle.down()
    turtle.setheading(360)  
    turtle.fillcolor("DeepPink")         
    turtle.begin_fill()
    turtle.color("Deeppink")              #Middle layer to be slightly smaller than the bottom layer
    turtle.forward(x/2-10) 
    turtle.setheading(270) 
    turtle.forward(y-2) 
    turtle.setheading(180) 
    turtle.forward(x/2-10)               #Could use (x-20) instead
    turtle.forward(x/2-10)               #Moving turtle forward with the full length minus 20 units
    turtle.setheading(90) 
    turtle.forward(y-2) 
    turtle.setheading(360)
    turtle.forward(x/2-10)               #Moving forward to complete the layer
    turtle.end_fill() 
    turtle.setheading(90)
    

"""Code for top layer of the cake"""
def cake_top(p, q):
    turtle.up()
    turtle.forward(q-7)                 #Moving to where the layer starts 
    turtle.setheading(360)
    turtle.down()
    turtle.fillcolor("Coral1")          #Setting color
    turtle.begin_fill()
    turtle.color("Coral1")
    turtle.forward(p/2-20) 
    turtle.setheading(270)
    turtle.forward(q-9)
    turtle.setheading(180) 
    turtle.forward(p/2-20) 
    turtle.forward(p/2-20) 
    turtle.setheading(90) 
    turtle.forward(q-9)
    turtle.setheading(360)
    turtle.forward(p/2-20) 
    turtle.end_fill()
    turtle.setheading(360)
    
"""Function to draw candle"""
def draw_candle():
    turtle.penup()
    turtle.pensize(3)                    #Adjusting the size of the pen
    turtle.goto(-25, 20)                 #The turtle move to the correct position
    turtle.pendown()                     #Pen is down to start drawing
    turtle.setheading(90)                
    turtle.fillcolor("red")              #Selecting the color of the bottom part of the candle
    turtle.begin_fill()
    turtle.color("red")
    turtle.forward(20)                   #starts to draw
    turtle.end_fill()

    turtle.fillcolor("yellow")           #Selecting the color of the top part of the candle
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(3)                     #drawing the circle on top of the bottom part of the candle with radius of 3
    turtle.end_fill()
    

"""Function to draw stars"""
def draw_star(size):
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(144)                    #angle of the stars
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)                     #repeating for 5 times to create a star
    turtle.forward(size)
    turtle.right(144)
    turtle.end_fill()
    

"""Add stars to each layer of the cake"""
def add_stars_to_layers():
    star_size = 8                        #the size of the stars

    """Add stars to the bottom layer""" 
    turtle.penup()
    turtle.pensize(1)                    #size of the lines
    turtle.goto(-75, -55)  # High on bottom layer
    turtle.pendown()            
    turtle.fillcolor("gold")      #color of the stars
    draw_star(star_size)

    turtle.penup()
    turtle.goto(-25, -55)
    turtle.pendown()
    draw_star(star_size)

    turtle.penup()
    turtle.goto(30, -55)
    turtle.pendown()
    draw_star(star_size)

    """Add stars to the middle layer"""
    turtle.penup()
    turtle.goto(-55, -25)  # Middle part of the middle layer
    turtle.pendown()
    draw_star(star_size)

    turtle.penup()
    turtle.goto(0, -25)
    turtle.pendown()
    draw_star(star_size)

    """Add stars to the top layer"""
    turtle.penup()
    turtle.goto(-25, 5)  #Middle part of the top layer
    turtle.pendown()
    draw_star(star_size)
    turtle.penup()
    turtle.home()


def main():
    turtle.penup()
    turtle.goto(-100, -80)  
    turtle.pendown()
    cake_bot(150, 45)  
    cake_middle(120, 35)  
    cake_top(90, 25)  

    draw_candle()

    # Add stars to each cake layer
    add_stars_to_layers()
    
    # Background color
    turtle.bgcolor("bisque2")
   
    print ("Close the canvas to exit!")
    turtle.hideturtle()
    turtle.done()

"""Input for length, width and color of table"""
l = int(input("Enter the length of the table (300 - 450): "))
w = int(input("Enter the width of the table (100 - 150): "))
leg_length = 0.4*l                                        
color = input ("Enter the color of your table: ")

"""Input for length and width of cake"""
len_cake = int(input("Enter the length of the cake (60-70): "))
wid_cake = int(input("Enter the width of the cake (30-40): "))



"""Placing restrictions on maximum and minimum length and width of table"""
if ( l < 300 or l > 450) :
    print ("Error, Please input positive values between 300 and 450 only")
if (w < 100 or w > 150): 
    print ("Error, Please input positive values between 100 and 150 only")
else:
    top_table(l,w,color)                            #Call function for table

"""Placing restrictions on maximum and minimum length and width of cake"""
if (len_cake < 60 or len_cake > 70):
    print ("Error, please enter a value between 60 and 70")
if (wid_cake < 30 or wid_cake > 40):
    print("Error, please enter a value between 30 and 40")
else:
    main()                                         #Call function for cake