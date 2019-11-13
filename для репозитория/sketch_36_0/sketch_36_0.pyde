def setup():
    size(500,500)
    smooth()
    strokeWeight(3)
    background(0)

i = 0
k = 1
flug = 1
myRandom = 0
myY1 = 0
myY2 = 0

def upDate():
    global i, k, flug, myRandom, myY1, myY2
    i +=k
    if i == 255:
        k=-1
    if i == 0:
        k=1    

def draw():
    global i, k, flug, myRandom, myY1, myY2
    stroke(i,20)
    myRandom = random(-20,20)
    myY1 = mouseY - myRandom
    myY2 = mouseY + myRandom
    line(0,myY1,500, myY2)
    upDate()
