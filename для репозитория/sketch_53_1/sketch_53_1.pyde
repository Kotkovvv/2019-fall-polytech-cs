counter = 0
cx = 0
cy = 0
fsize = 0

class FunnyRect():

    def setCenter(self, x,y):
        self.cx = x
        self.cy = y

    def setSize(self, size):
        self.size = size

    def render(self):
        rect(self.cx, self.cy, self.size, self.size)
        
    def colors(self, h):
        fill(h)


funnyRect = FunnyRect()
f = FunnyRect()

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    f.setSize(50)

def draw():
    background(255)
    global counter
    
    objX = mouseX +sin(counter)*150
    objY = mouseY +cos(counter)*150
    
    funnyRect.colors(50)
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    f.colors(180)
    f.setCenter(objX, objY)
    f.render()
    counter +=0.05
