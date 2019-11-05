from tkinter import *
import turtlefigure
import turtle
from turtle import *
import random 
from PIL import ImageGrab, Image
import os
import time


open("README.rtf").read()

root = Tk()
root.geometry("1050x800+600+600")
root.title("Turtle Fractal Generator")
root.config(bg = "#160E2B")

colors = ["#03CDD2", "#A26DCB", "#FB7299"]


'''------------------------BUTTON HANDLERS-------------------------- '''

def onClearF():
     entryOrder.delete(0, END)
     entrylength.delete(0, END)
     info.set("Please use the Control Panel above to insert an Order (number), Length (number) and select a Figure."
              " \nAdditional Info will show here when the drawing has started."
              "\nRemember, the higher the order, the more intricate the figure but the longer it will take to finish. "
              "\nA larger value for length will make the figure larger.")
     pen.reset()
     pen.color(random.choice(colors))
     pen.shape("turtle")
     pen.speed(0)
     pen.width(2)
     pen.up();pen.setx(-150);pen.sety(-75);pen.down()
          
#end clearF


def onDrawF():
     print("Drawing start")
    
     n = int(orderStr.get())
     l = int(lengthStr.get())

     turtleIndex = turtleList.index(turtleStr.get())
     if turtleIndex == 0:
         info.set("The Sierpinski Triangle is a fractal with the overall shape of an equilateral triangle."
                  " \nIt is subdivided recursively into smaller equilateral triangles. "
                  "\nThe Triangles are created with a 120 degree angle.")
         turtlefigure.gasket(n, l, pen)
         pen.ht()
         
     if turtleIndex == 1:
         info.set("This square fractal is a Sierpinski fractal. Instead of using a 120 degree angle "
                  "(which would create a triangle) it uses a 90 degree angle.")
         turtlefigure.gasket4(n, l, pen)
         pen.ht()

     if turtleIndex == 2:
         info.set("This figure is a Sierpinski Carpet. \nUnlike the rest of the figures "
                   "this figure is made by utlilzing the 'fill' option.")
         pen.color("#6DC1FF")
         turtlefigure.Carpet(n, l, pen)
         pen.ht()

     if turtleIndex == 3:
         info.set("This fractal is a Binary Tree. \nUnfortunately, it has fallen down."
                   "\nPlease note, I DO believe in saving the trees.")
         turtlefigure.tree(n, l, pen)
         pen.ht()
          
     if turtleIndex == 4:
         info.set("Here we have a dandelion. For better results, "
                   "choose a higher order number.")
         turtlefigure.tree4(n, l, pen)
         pen.ht()
          
     if turtleIndex == 5:
         info.set("The Intricate Fern fractal resembels a growing fern and is a particularly beautiful figure.")
         turtlefigure.fern(n, l/2, pen)
         pen.ht()
          
     if turtleIndex == 6:
         info.set("This is a flake that is created through the use of a 60 degree "
                   "and 120 degree koch curve.")
         pen.up();pen.setx(-150);pen.sety(150);pen.down()
         turtlefigure.flake(n, l, pen)
         pen.ht()
          
     if turtleIndex == 7:
         info.set("The antiflake is created by turning the pen to the left after "
                   "the first koch curve rather than right.")
         turtlefigure.antiflake(n, l, pen)
         pen.ht()
          
     if turtleIndex == 8:
         info.set("This is a Circular fractal. It is created by drawing an outer circle of radius (r), "
                   "then drawing 4 smaller circles that are half of the radius. "
                   "\n we would recommend keeping the length less than 425!")
         pen.up();pen.setx(0);pen.sety(-150);pen.down()
         turtlefigure.c(n, l/2, pen)
         pen.ht()
          
     if turtleIndex == 9:
         info.set("This is my own circular fractal using 2 circels that are half of the outer circle "
                   "radius and 2 circles that are one third of the radius.")
         pen.up();pen.setx(0);pen.sety(-150);pen.down()
         turtlefigure.c1(n, l/2, pen)
         pen.ht()
          
     if turtleIndex == 10:
         info.set("This is a cesaro square. The tears in the shape are 10 degrees.")
         turtlefigure.cesasqre(n, l*2, pen)
         pen.ht()
          
     if turtleIndex == 11:
         info.set("This hexagaon was created with a Koch curve of 90 degrees and "
                   "an overal recursion of 60 degrees to create the hexagon.")
         turtlefigure.HexShield(n, l*1.5, pen)
         pen.ht()
          
     if turtleIndex == 12:
         info.set("This triangle was created with a Koch curve of 90 degrees and "
                   "an overal recursion of 120 degrees to create the triangle.")
         turtlefigure.TriBadge(n, l*2, pen)
         pen.ht()

          
     print("Drawing Finished")      
#end drawF


def onSaveF():
     im = ImageGrab.grab((780,225,2225,1650))
     im.save(os.getcwd() + "\\canvas_snap_" + str(int(time.time()) ) + ".png", "PNG")
     info.set("You have saved your canvas as a .png file! \nThe file has been saved "
              "in your current working directory, with the name 'canvas_snap' followed "
              "by the the number of seconds passed since epoch. \nPssst...press the "
              "'Clear' button to see the instructions again.")
     

     print("Image has been saved")
    


'''------------------------------- INTERFACE COMPONENTS----------------------------------'''
             
root.title("Turtle Fractal")

label = Label(root, text = "Turtle Fractal Generator",
              font = "TkMenuFont 18 bold",
              fg = "white", bg = "#160E2B")

label.grid(row = 0, column = 1, columnspan = 2)

canvasFrame = LabelFrame(root, text = "Canvas Space",
                         font = "TkMenuFont 14 bold",
                         fg = "purple",
                         width = 510, height = 510)


canvas = Canvas(canvasFrame, width = 700, height = 700)
canvas.pack()  
canvasFrame.grid(row = 1,column = 0,
                 ipadx = 2, ipady = 2,
                 padx =5, pady =5,
                 columnspan = 4, rowspan = 4)

controlFrame = LabelFrame(root, text = "Control Panel",
                          font = "TkMenuFont 14 bold",
                          fg = "purple")

controlFrame.grid(row = 0, column = 5, columnspan = 2, rowspan = 3, ipadx = 2, ipady = 2, padx =5, pady =5)


labelOrder = Label(controlFrame, width = 15,text = "Order")
labelOrder.grid(row = 1, column =0)

orderStr = StringVar()
entryOrder = Entry(controlFrame, width = 15,textvariable = orderStr)
entryOrder.grid(row = 1, column = 1)

labelLength = Label(controlFrame, width = 15,text = "Length")
labelLength.grid(row = 2, column =0)

lengthStr = StringVar()
entrylength = Entry(controlFrame, width = 15,textvariable = lengthStr)
entrylength.grid(row = 2, column = 1)

labelFigure = Label(controlFrame,width = 15, text = "Figure")
labelFigure.grid(row = 3, column =0)



'''----------------------------DROP DOWN LIST ------------------------------------'''

turtleList = ["Sierpinski Triangle", "Sierpinski Square", "Sierpinski Carpet", "Tree", "Dandelion", "Fern", "Flake",
              "Antiflake", "Circle", "Custom Circle", "Cesaro", "Hex Shield", "Tri Shield"]
turtleStr = StringVar()
turtleOptionMenu = OptionMenu(controlFrame, turtleStr, *turtleList)
turtleOptionMenu.grid(row = 3, column = 1)
turtleOptionMenu["width"] = 15
turtleOptionMenu.configure(takefocus=1)


'''---------------------------- WIDGET BUTTONS ----------------------------------'''

clearButton = Button(controlFrame, text = "Clear", width = 10, command = onClearF, cursor = "poof")
clearButton.grid(row = 4, column = 0)
clearButton.config(highlightbackground = "#FB7299", bg = "#FB7299", activebackground = "#FB7299")

drawButton = Button(controlFrame, text = "Draw", width = 10,command = onDrawF, cursor = "pencil")
drawButton.grid(row = 4, column = 1)
drawButton.config(highlightbackground = "#03CDD2", bg = "#03CDD2", activeforeground = "#03CDD2")


'''-------------------------------TEXT BOX----------------------------------------'''

textFrame = LabelFrame(root, text = "Additional Info",
                       font = "TkMenuFont 14 bold",
                       fg = "purple",
                       width = 200, height = 150)
textFrame.grid(row = 3, column = 5, columnspan = 2, rowspan = 4, ipadx = 5, ipady = 5, padx =5, pady =5)

info = StringVar()
info.set("Please use the Control Panel above to insert an Order (number), Length (number) and select a Figure."
         " \nAdditional Info will show here when the drawing has started. "
         "\nRemember, the higher the order, the more intricate the figure but the longer "
         "it will take to finish. \nA larger value for length will make the figure larger.")

infoLabel = Label(textFrame, textvariable = info, wraplength = 250 )
infoLabel.pack()


'''-------------------------------SAVE BOX----------------------------------------'''

saveFrame = LabelFrame(root, text = "Image Capture",
                       font = "TkMenuFont 14 bold",
                       fg = "purple",
                       width = 200, height = 50)
saveFrame.grid(row = 1, column = 5, columnspan = 2, rowspan = 4, ipadx = 5, ipady = 5, padx =5, pady =5)

saveButton = Button(saveFrame, text = "Save Drawing", width = 15,command = onSaveF, cursor = "heart")
saveButton.grid(row = 0, column = 0, columnspan=2, pady = 10, padx = 15)
saveButton.config(highlightbackground = "#A26DCB", bg = "#A26DCB", activebackground = "#A26DCB")


'''----------------------------TURTLE CONTROLS-------------------------------'''

pen = turtle.RawTurtle(canvas)
pen.color(random.choice(colors))
pen.shape("turtle")
pen.speed(0)
pen.width(2)
pen.up();pen.setx(-150);pen.sety(-75);pen.down()

root.mainloop()
