import turtle

startposx=int(input("Choose the turtle's x position:\n"))
print(f"x position: {startposx}")
startposy=int(input("Choose the turtle's y position:\n"))
print(f"y position: {startposy}")

linecolor=input("Choose your line color:\n")
print(f"Line color: {linecolor}")
fillcolor=input("Choose your fill color:\n")
print(f"Fill color: {fillcolor}")

length=int(input("Choose your length:\n"))
print(f"Length: {length}")
depth=int(input("Choose the amount of iterations:\n"))
print(f"Iterations: {depth}")

def drawsierpinski(length,depth):
    t.fillcolor(f"{fillcolor}")
    t.begin_fill()

    if depth or length<0:
        raise ValueError("Length/iteration value cannot be negative.")

    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)

    else:
        drawsierpinski(length/2,depth-1)
        t.fd(length/2)
        drawsierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        drawsierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)
    t.end_fill()

def setpos():
    t.pu()
    t.setpos(startposx,startposy)
    t.pd()

window=turtle.Screen()
window.title("Sierpiński Triangle")
t=turtle.Turtle()

setpos()
t.pen(pencolor=f"{linecolor}", speed=4, pendown=True)
drawsierpinski(length, depth)
window.exitonclick()