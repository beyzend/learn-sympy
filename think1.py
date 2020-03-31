import turtle


def make_window(color, title):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window


def make_turtle(color, size):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal

def DrawCornerEdge(pen, angle, edge):
    pen.forward(edge)
    pen.left(angle)
    pen.forward(edge)

def DrawPoly(pen, nSides, sideLength):
    """This function will draw a n sided polygon. 
    
    It draw the n side polygons by draw n edge-corners. 
    """
    pen.pendown()
    deltaAngle = 360.0 / nSides
    for _ in range(nSides):
        DrawCornerEdge(pen, deltaAngle, sideLength / 2)
    pen.penup()
def doDrawPoly(pen):
    sideLength = 10.0
    n = 5
    sides = 8
    pen.speed(1000)
    pen.penup()
    pen.goto(0, 0)

    for i in range(n):
        pen.pendown()
        pen.left(90)
        DrawPoly(pen, sides, sideLength)
        pen.penup()
        pen.right(90)
        pen.forward(sideLength / 2)
        sideLength = sideLength * 2


def DrawSquares(pen, sideLength):
    """This function will draw a origin centered square"""
    n = 5
    sides = 4
    pen.speed(100)
    #Will draw a square with 4 sub squares.
    pen.penup()
    pen.goto(0, 0)
    sideLengthHalf = sideLength / 2
    #Draw 2 subsquares
    #Face up
    pen.left(90)
    for _ in range(2):
        pen.left(180) #face down
        pen.forward(-sideLengthHalf / 2)
        DrawPoly(pen, sides, sideLengthHalf)
        pen.forward(sideLengthHalf)
        DrawPoly(pen, sides, sideLengthHalf)
        pen.goto(0, 0)
        pen.left(180)
        pen.left(90)
        pen.forward(sideLengthHalf)
        pen.left(-90)
    pen.goto(0, 0)
    pen.left(-90)

def doDrawRotatedSquares(pen):
    sideLength = 400.0
    n = 20
    deltaAngle = 360.0 / n
    print("deltaAngle: {}".format(deltaAngle))
    color = ["blue", "hotpink", "purple", "red"]
    colorIndex = 0
    #draw rotated squares
    for i in range(n):
        #Draw each sequare
        pen.color(color[colorIndex % len(color)])
        colorIndex += 1
        pen.goto(0, 0)
        DrawSquares(pen, sideLength)
        pen.left(deltaAngle)
        print("heading: {}".format(pen.heading()))

def doExcercise(tess):
    sideLength = 0.1
    tess.penup()
    #Draw 5 squares on the screen.
    #Goto initial position. That is lower right corner facing up.
    tess.goto(0, 0)
    tess.goto(sideLength*0.5, -sideLength*0.5)
    tess.left(90) 
    for i in range(20):
        #Move to start position:  turn to face draw direction, then move 
        #to a corner
        halfLength = 0.5*sideLength
        tess.pendown()
        #to an edge
        DrawSquare(tess, sideLength)
        tess.penup()
        tess.right(90)
        tess.forward(halfLength) 
        tess.left(90)
        tess.backward(halfLength)
        sideLength=sideLength*2


penSize = 3

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("blue", penSize)

#doExcercise(tess)
#doDrawPoly(tess)
doDrawRotatedSquares(tess)
wn.mainloop()
