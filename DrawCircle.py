import turtle
import random
import math

def draw_circle(instr, dist):
    swidth, sheight = 300, 300
    tx, ty, txtsize = [0] * 3

    turtle.title('거북아 그 속도론 멀리 못 도망가')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth, sheight)
    turtle.penup()

    angle = 0
    value = int(360/len(instr))

    for ch in instr:
        rad = 3.141592 * angle / 180
        tx = dist * math.cos(rad)
        ty = dist * math.sin(rad)
        angle += value

        r = random.random()
        g = random.random()
        b = random.random()
        txtSize = random.randrange(20,21)
        turtle.goto(tx,ty)
        turtle.pencolor(r,g,b)
        turtle.write(ch, font=('맑은고딕', txtsize, 'bold'))

    turtle.done()
