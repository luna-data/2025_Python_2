import turtle 
t=turtle.Pen()
t.speed(10)

t.reset()
for x in range(1,10):
    t.color(0.9,0.75,0)
    t.begin_fill()

    t.forward(120)
    t.left(175)

    t.forward(120)
    t.left(225)

    t.end_fill()
for x in range(1,10):
    t.color(0,0,0)
    t.forward(120)
    t.left(175)

    t.forward(120)
    t.left(225)


turtle.done()