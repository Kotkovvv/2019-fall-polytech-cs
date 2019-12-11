coint = 0

def setup():
    background(100)
    smooth()
    img1 = loadImage("data/003.jpg")
    img2 = loadImage("data/002.jpg")
    size(800,800)
    global img1, img2
    
def mouseClicked():
    global coint
    if mouseButton == LEFT:
        coint += 5
        if coint < 0:
            coint = 0
    if mouseButton == RIGHT:
        coint -= 5
        if coint > 100:
            coint  = 100    
def draw():
    myTint000 = map(coint, 0, 100, 0, 255)
    myTint001 = map(coint, 0, 100, 255, 0)
    tint(255, myTint001)
    image(img1, 0, 0)
    tint(255, myTint000)
    image(img2,0,0)
