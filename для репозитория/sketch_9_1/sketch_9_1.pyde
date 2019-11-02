size(600,600)
noLoop()

def abc(a):
    rotate(PI/4)
    fill(a)
    rect(0,50,150,50)
    rect(50,0,50,150)


background(20)
smooth()
noStroke()

pushMatrix()
translate(100,0)
rotate(PI/4)
abc(180)
popMatrix()

pushMatrix()
translate(220,100)
rotate(PI/6)
scale(2)
abc(220)
popMatrix()

pushMatrix()
translate(520,350)
rotate(PI/3)
scale(1.4)
abc(80)
popMatrix()
