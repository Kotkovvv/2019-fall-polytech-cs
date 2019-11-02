def setup():
    size(300,300)
    smooth()
    strokeWeight(30)
    background(0)
    #noLoop(0)

def draw():
    stroke(frameCount)
    line(frameCount+100,frameCount+100,200+frameCount,200+frameCount)
    line(200+frameCount,100+frameCount,100+frameCount,200+frameCount)
