import turtle


def gajurel(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)


class Cartoon:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(gajurel)

    def meme(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def aankha1(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def aankha2(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mukh(self, x, y):
        self.meme(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()
        #
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        self.meme(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        #

        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        #
        self.meme(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        #
        self.meme(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    #
    def gaala1(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.meme(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def gaala2(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.meme(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def kaan1(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def kaan2(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def jiu(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        #
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        #
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        #
        t.seth(150)
        t.circle(150, 70)

        #
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        # print(t.pos())

        #
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        #
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        #
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        #
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        #
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        #
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        #
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        self.meme(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        #
        self.meme(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        #
        self.meme(168, 134)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        ##############
        # print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        #
        t.fillcolor('#923E24')
        self.meme(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        self.topi(-134.07, 147.81)
        self.mukh(-5, 25)
        self.gaala1(-126, 32)
        self.gaala2(107, 63)
        self.kaan1(-250, 100)
        self.kaan2(140, 270)
        self.aankha1(-85, 90)
        self.aankha2(50, 110)
        t.hideturtle()

    def topi(self, x, y):
        self.meme(x, y)
        t = self.t
        t.fillcolor('#CD0000')
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        # print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        self.meme(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor('#444444')
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        self.meme(-58, 270)
        t.pencolor('#228B22')
        t.dot(35)

        self.meme(-30, 280)
        t.fillcolor('#228B22')
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor('#000000')

    def start(self):
        self.jiu()


def main():
    print('Painting the Cartoon... ')
    turtle.screensize(800, 600)
    turtle.title('Cartoon')
    cartoon = Cartoon()
    cartoon.start()
    turtle.mainloop()


if __name__ == '__main__':
    main()

'''
Explanation:
First Part ( Import, gajurel() and part 1 of the class ):
First, import the turtle module and create a function named “gajurel” with the parameters (x, y). Inside this function, set the x of the turtle to “x” and y of the turtle to “y.” Then, print the x and y.
Create a class named Cartoon. Inside this class, create an initializer __init__. Inside this function, set “t” as the turtle and set the pen size to 3 and speed to 9. Never forget that functions inside a class always have a parameter “self.” Now, on drag, call the gajurel function.
Create another function named meme() with the parameters self, x, and y. inside this function, pick the pen up and go to (x, y), and put the pen down.
Likewise, create another function named aankha1() with the parameters self, x, and y. Inside this function, call the meme() function with the arguments (x, y). Set “self.t” as “t”. Call the seth() method with the angle of 0 degrees and fill the part with the color#333333 and begin the fill. Draw a circle(22) and end the fill. Again, call the meme() function with the arguments (x, y+10) and fill the part with the color #000000 ( black ), and begin the fill. Create a circle(10) and end the fill. Again, call the meme() function with the arguments (x+6, y+22) and fill the part with the color #ffffff ( white ) and begin the fill. Create a circle(10) and end the fill.
Similarly, create another function named aankha2() with the parameters self, x, and y. Inside this function, call the meme() function with the arguments x and y. Then, set “self.t” as “t.” Now, call the seth() method with the angle of 0 and fill the part with the color #333333 and begin the fill. Draw a circle(22) and end the fill. Continuing, call the meme() function with the arguments x, y+19 and fill the part with the color #00000 ( black ) and begin the fill. Draw a circle(10) and end the fill. Similarly, call the meme() function again with the arguments (x-6, y + 22) and fill the part with the color #ffffff ( white ) and begin the fill. Draw a circle(10) and end the flll.
Second Part ( Class Part – 2 ):
Inside the same class, create a function name mukh() with the parameters self, x, y. Inside this function, call the meme(x, y) and fill the part with the color #88141D and begin the fill. Create two empty lists with the variables named l1 and l2. Call the seth(190) and (a = 0.7). Create a for loop with the range of 28 and add 0.1 to a and move the turtle right(3), fd(a), and append to l1 the turtle’s position. Call the meme(x, y) and seth(10) and (a =0.7). Create another for loop with the range of 28 and do the same as above but with l2. Then call the seth(10), circle(50, 15), Left(180) and circle(-50, 15) for as in the code above in the line 96. After calling the meme(17, 54) again and fill the part with the color#DD716F and begin the fill. Call the seth() method with the 145 angles, circle(40, 86), and pick the pen up. Now, create a for loop at the range of {reversed(l1[:20])}; goto { t.goto(pos[0], pos[1]+1.5) }. Again create a for loop with the range of { l2[:20] }; and go to { t.goto(pos[0], pos[1]+1.5) }.
Again, call a function named gaala1 with the parameters of self, x, y. Inside this function, set the tracer to false and call the meme(x, y), seth(300), fill the part with the color #dd4d28 begin the fill. Set the value of “a” to 2.3 and create a for loop with the range of 120; create an if function which will sub 0.05 from a and lt(3),fd(a) of I is between 0 and 30 or 60 and 90. else; add 0.05 to a and lt(3),fd(a).
Third Part ( Class Part – 3 ):
Moreover, create a function gaala2(self, x, y). Inside this function, call the meme(x, y), seth(60), fill the color #DD4D28 and begin the fill and do the same as above with gaala2() as in gaala1().
Then, create a kaan1(self, x, y) function; call the meme(x, y), fill the color black and begin the fill. call t.seth(330), t.circle(100, 35), t.seth(219), t.circle(-300, 19),t.seth(110), t.circle(-30, 50), t.circle(-300, 10), t.end_fill(). Do the same with kaan2()
Create a jiu() function; fill the color as #f6202f and begin the fill. Pick the pen up and circle(130, 40). Put the pen down and draw a circle(100, 105), move left at an angle of 180, and draw another circle(-100, 5). The values for the methods will change but do the code as above.
Last Function in the class:
Create a topi() function with the parameters of self,x,y. Inside this function, call meme(x, y) and fill the color #CD0000 and begin the fill. Call seth(200),t.circle(400, 7),t.left(180), t.circle(-400, 30),t.circle(30, 60),t.fd(50),t.circle(30, 45), t.fd(60),t.left(5), t.circle(30, 70), t.right(20),t.circle(200, 70),t.circle(30, 60), t.fd(70), t.right(35),t.fd(50),t.circle(8, 100),t.end_fill(),self.meme(-168.47, 185.52),t.seth(36) ,t.circle(-270, 54),t.left(180),t.circle(270, 27),t.circle(-80, 98).
Create a function name start and call the function jiu() inside it.
Last Part:
Lastly, create a function main. Inside this function, set the screen size to 800 / 600. Then, create an object cartoon with the Cartoon() class and call the function start() through the cartoon object. Close the mainloop as in Tkinter.
At last, create a module source as this is the main program and call the main() function inside it.
Thank You for reading till the end. Comment you queries if you have any.
'''