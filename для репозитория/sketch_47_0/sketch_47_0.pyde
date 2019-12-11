counter = 1
counter1 = 1
cx = 250
cy = 250
cR = 100
def setup():
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)

def draw():
    global counter1, cx, cy, cR, counter
    
    stroke(0,30)
    
    nx = sin(counter1)*cR + cx
    ny = cos(counter1)*cR + cy
    
    x1 = nx - sin(counter)*300
    y1 = ny - cos(counter)*300
    x2 = nx + sin(counter)*300
    y2 = ny + cos(counter)*300
    
    line(x1, y1, x2, y2)
    
    counter +=0.1
    if counter > 2*PI:
        counter = 0
    
    counter1 += mouseX / float(width*2)
    
    if counter1 > 2*PI:
        counter1 = 0
