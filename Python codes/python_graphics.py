import random
import time
from graphics import *
  
def main():
    
    workArea = GraphWin('Growing Circles', 400, 400) # give title and dimensions
    col_arr=["violet","indigo","blue","green",
             "yellow","orange","red","pink",
             "brown","purple","gray","maroon",
             "black","lime","cyan","thistle",
             "orchid","tomato","gold","aqua",
             "fuchsia","navy","plum","crimson",
             "lightcoral","royalblue",
             "deeppink"]
    msg=Text(Point(150,10),"Double Click to Start a new circle")
    msg.draw(workArea)
    i=1
    x=workArea.width/2
    y=workArea.height/2
    clk=True
    while clk:
        rad=20
        #get a color from colors array
        clr=col_arr[random.randrange(len(col_arr))]
        #let the circle grow unless you double click
        while not workArea.checkMouse():
            cir=Circle(Point(x,y),rad)
            cir.setFill(clr) 
            cir.setOutline(clr)
            cir.draw(workArea)
            #increment radius 
            rad=rad+1
            #add delay
            time.sleep(0.08)
            
        msg=Text(Point(150,10),"Double Click to Start a new circle")
        msg.draw(workArea)
        # redefine center of circle where you click
        ch=workArea.getMouse()
        x=ch.x
        y=ch.y
        
        
    workArea.getMouse()
    workArea.close() # close the workArea window

main()