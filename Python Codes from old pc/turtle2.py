from turtle import*
bgcolor('black')
speed(11)
hideturtle()
for i in range(200):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    left(3)
    backward(3)
done();