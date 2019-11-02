def setup():
    size(300,300)
    smooth()
    strokeWeight(30)
    stroke(100)
    #noLoop(0)

def draw():
    background(0)
    line(100,100,200,200)
    line(200,100,100,200)
    println(frameCount)
