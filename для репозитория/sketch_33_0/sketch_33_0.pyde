def setup():
    background(255)
    size(500, 500)
    smooth()
    
l1x1=0
l1y1=0
def setup():
    size(300,300)
    smooth()
    strokeWeight(30)
    background(0)

i = 0
k = 1

def draw():
    global i, k
    stroke(i,20)
    line(mouseX, mouseY, random(0,500),500)
    i +=k
    if i == 255:
        k=-1
    if i == 0:
        k=1

def keyPressed():
    if key == "s":
        saveFrame("meProcessing.png")
