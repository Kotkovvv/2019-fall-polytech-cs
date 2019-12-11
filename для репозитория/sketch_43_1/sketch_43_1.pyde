counter = 0
cx = 875
cy = 400
nx = 0
ny = 0
counter1 = 0
cR = 250
ncx = 0
ncy = 0
i=5
def setup():
    size(1750,800)
    smooth()
    background(0)
    strokeWeight(1)
    
def oneLineDraw(ncx, ncy):
    global cx,counter,cy,nx,ny,counter1,cR,i
    x1 = ncx - sin(counter1)*100
    y1 = ncy - cos(counter1)*100
    x2 = ncx + sin(counter1)*100
    y2 = ncy + cos(counter1)*100
    line(x1,y1,x2,y2)
    
counter=0
cx=0
cy=0
nx=0
ny=0
def setup():
    size(500,500)
    smooth()
    background(0)
    strokeWeight(1)

def draw():
    global counter,cx,cy,nx,ny
    stroke(200,5)
    for si in range(0,6,1):
        for ci in range(0,6,1):
            nx=ci*80+50
            ny=si*80+50
            point(nx,ny)
            x1=nx-sin(counter)*(50)
            y1=ny-cos(counter)*(50)
            x2=ny+sin(counter)*(50)
            y2=nx+cos(counter)*(50)
            line(x1,y1,x2,y2)
    
    counter += 0.1
    if counter > 2*PI:
        counter=0
