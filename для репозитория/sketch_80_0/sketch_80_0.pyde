def setup():
    background(100)
    smooth()
    size(1080,1080)
    noStroke()
    img1 = loadImage("data/build1.jpg")
    img4 = loadImage("data/build.jpg")
    global img1, img4
    
    
def draw():
    if frameCount == 1:
        image(img1, 0, 0)
        
    va12 = int(random(0,150))
    va13 = int(random(0,150))
    
    img2 = img1.get(mouseX + va12,0,20, height)
    img3 = img1.get(mouseX + va13,0,5, height)
    
    blendMode(SUBTRACT)
    tint(255, 20)
    image(img2, mouseX + va12, random(0,height))
    
    noTint()
    blendMode(BLEND)
    image(img3, mouseX - va13, 0)
    
    image(img4,0,0)
