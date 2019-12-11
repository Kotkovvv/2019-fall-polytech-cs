def setup():
    background(100)
    smooth()
    noStroke()
    img1 = loadImage("data/003.jpg")
    img2 = loadImage("data/002.jpg")
    size(800,800)
    global img1, img2
    
def draw():
    if frameCount == 1:
        image(img2, 0,0)
    
    pointSize = map (mouseX, 0, width, 0, 100)
    pointAlpha = map(mouseY, 0, height, 0, 255)
    
    x = random(img1.width)
    y = random(img1.height)
    loc = int(x + y*img1.width)
    img1.loadPixels()
    r = red(img1.pixels[loc])
    g = green(img1.pixels[loc])
    b = blue(img1.pixels[loc])
    
    fill(r,g,b,pointAlpha)
    ellipse(x,y,pointSize,pointSize)
    
    tint(255,2)
    image(img2, 0,0)
    filter(BLUR, 3)
