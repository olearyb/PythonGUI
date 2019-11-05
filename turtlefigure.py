from turtle import *
import math
import random
'''
pen = Pen()
pen.color("#06CDF4")
pen.speed(0)
pen.width(2)

pen.up();pen.sety(-200);pen.down()

screen = Screen()
screen.bgcolor("gray20")
'''

colors = ["#03CDD2", "#A26DCB", "#FB7299"]
colors2 = ["#5BC0BE", "#6FFFE9"]

def gasket(n, l, pen):

    
    # draw a triangle
    if n==0 or l<2:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
            
        return

    # for each triangle
    for i in range(3):
        gasket(n-1, l/2, pen)
        pen.forward(l)
        pen.left(120)
        pen.color(random.choice(colors))




def gasket4(n, l, pen):
    # draw a square fractal
    if n==0 or l<2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)

        return

    # for each square
    for i in range(4):
        gasket4(n-1, l/3, pen)
        pen.forward(l)
        pen.left(90)
        pen.color(random.choice(colors))

    return

# gaskets.py

def tree(n,l, pen):

    if n==0 or l<2 :
        return
    # endif
    
    pen.forward(l)
    pen.left(45)
    tree(n-1, l/2, pen)
    pen.color(random.choice(colors))
    pen.right(90)
    tree(n-1, l/2, pen)
    pen.color(random.choice(colors))
    pen.left(45)
    pen.backward(l)

# end tree

# TurtleFigures.py

def tree4(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.color(random.choice(colors))
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.color(random.choice(colors))
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.color(random.choice(colors))
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.color(random.choice(colors))
     
     pen.left(90)
     pen.backward(l)

#end 


def fern(n,l, pen):
     if n == 0 or l < 2:
          return
     #endif
     pen.forward(0.3*l)
     pen.left(45)
     fern(n-1, 0.4*l, pen)
     pen.color(random.choice(colors))
     pen.right(45)
     pen.forward(0.7*l)
     pen.color(random.choice(colors))
     pen.right(30)
     fern(n-1, 0.5*l, pen)
     pen.color(random.choice(colors))
     pen.left(30)
     pen.forward(l)
     pen.right(15)
     fern(n-1, 0.7*l, pen)
     pen.color(random.choice(colors))
     pen.left(15)
     pen.backward(2*l)
#end fern

def koch(n, l, pen):
     if n == 0 or l < 2:
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3, pen)
     pen.left(60)
     pen.color(random.choice(colors))
     koch(n-1,l/3, pen)
     pen.right(120)
     pen.color(random.choice(colors))
     koch(n-1, l/3, pen)
     pen.left(60)
     pen.color(random.choice(colors))
     koch(n-1,l/3, pen)

#end koch

def flake(n,l, pen):
     for i in range(3):
          koch(n,l, pen)
          pen.right(120)
          pen.color(random.choice(colors))
     #end for
#end flake

def antiflake(n,l, pen):
     for i in range(3):
          koch(n,l, pen)
          pen.left(120)
          pen.color(random.choice(colors))
     #end for
#end flake




def c(n, l, pen):
     if n == 0 or l < 2:
          pen.circle(l)
          return
     #endif
     pen.circle(l)
     for i in range (4):
        c(n-1, l/2, pen)
        pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
    #end for

#end circle

def c1(n, l, pen):
     if n == 0 or l < 2:
          pen.circle(l)
          return
     #endif
     pen.circle(l)
     pen.color(random.choice(colors))

     for i in range(2):
         c1(n-1, l/2, pen)
         pen.color(random.choice(colors))
         pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
         c1(n-1, l/3, pen)
         pen.color(random.choice(colors))
         pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()

         #end for
    #end circle

'''
def c2(n, l, pen):
     if n == 0 or l < 2:
          pen.circle(l)
          return
     #endif
     pen.circle(l)
     c2(n-1, l/4, pen)
     pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
     c2(n-1, l/4, pen)
     pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
     c2(n-1, l/4, pen)
     pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
     c2(n-1, l/4, pen)
     pen.up(); pen.forward(l); pen.left(90); pen.forward(l); pen.down()
     
    #end for

#end circle
'''

# cesaro torn line
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

def cesaro(n, l, pen):
    if n == 0 or l < 2:
        pen.forward(l)
        return
    #endif
    cesaro(n-1, l/3, pen)
    pen.left(85)
    pen.color(random.choice(colors))
    cesaro(n-1, l/3, pen)
    pen.right(170)
    pen.color(random.choice(colors))
    cesaro(n-1, l/3, pen)
    pen.left(85)
    pen.color(random.choice(colors))
    cesaro(n-1, l/3, pen)

    # end for
# end cesaro

# cesaro square
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

def cesasqre(n, l, pen):
    if n == 0 or l < 2:
        pen.forward(l)
        return
    for i in range(4):
        cesaro(n-1, l/3, pen)
        pen.left(85)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.right(170)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.left(85)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.left(90)
        pen.color(random.choice(colors))
        # end for
# end cearo square

def anticesasqre(n, l, pen):
    if n == 0 or l < 2:
        pen.forward(l)
        return
    for i in range(4):
        cesaro(n-1, l/3, pen)
        pen.right(85)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.left(170)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.right(85)
        pen.color(random.choice(colors))
        cesaro(n-1, l/3, pen)
        pen.right(90)
        pen.color(random.choice(colors))
        # end for
# end cearo square

 
def blocks(n, l, pen):
     if n == 0 or l < 2:
          pen.forward(l)
          return
     #endif
     blocks(n-1,l/3, pen)
     pen.color(random.choice(colors))
     pen.right(90)
     blocks(n-1,l/3, pen)
     pen.color(random.choice(colors))
     pen.left(180)
     blocks(n-1, l/3, pen)
     pen.color(random.choice(colors))
     pen.right(90)
     blocks(n-1,l/3, pen)
     pen.color(random.choice(colors))

#end blocks

def HexShield(n,l, pen):
     for i in range(6):
          blocks(n,l, pen)
          pen.left(60)
          pen.color(random.choice(colors))
     #end for
#end HexShield


def TriBadge(n, l, pen):
    for i in range(3):
        blocks(n, l, pen)
        pen.left(120)
        pen.color(random.choice(colors))
    # end for
# end TriBradge

def Carpet(n, l, pen):
    if n == 0 or l < 2:
        pen.width(1)
        pen.fillcolor("#B2DDFF")
        pen.begin_fill()
        for _ in range (4):
            pen.forward(l)
            pen.left(90)
        pen.end_fill()
    else:
        for i in range(4):
            Carpet(n-1, l/3, pen)
            pen.forward(l/3)
            Carpet(n-1, l/3, pen)
            pen.forward(l/3)
            pen.forward(l/3)
            pen.left(90)
# end for
    
        
        
