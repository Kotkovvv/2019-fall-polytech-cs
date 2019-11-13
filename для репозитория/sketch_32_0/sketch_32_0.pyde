def setup():
    background(255)
    size(500, 500)
    smooth()
    
l1x1=0
l1y1=0
l1x2=500
l1y2=500
flug=1

def setup():
    background(255)
    size(500, 500)
    smooth()
    
l1x1=0
l1y1=0
l1x2=500
l1y2=500
flug=1

mr = 10
mg = 150
mb = 100

def draw():
    global l1x1, l1y1, l1x2, l1y2, flug, mr, mg, mb
    background(0)
    strokeWeight(120)
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
    line(mouseX-50, mouseY-50, 100 + mouseX-50, 100+mouseY -50)
    line(100+mouseX-50, mouseY-50, mouseX-50, 100+mouseY-50)
    i +=k
    if i == 255:
        k= -1
    if i ==0:
        k = 1
