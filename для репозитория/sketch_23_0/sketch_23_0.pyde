size(500,500)
smooth()
background(255)
noLoop()
noStroke()
ellipseMode(CENTER)

background(255)
border=50
nw=width-2*border
nh=height-2*border
number=5
nWstep=nw/number
nHstep=nh/number
for i in range (0,5,1):
    for j in range (0,5,1):
        x=border+j*nWstep+nWstep/2
        y=border+i*nHstep+nHstep/2
        size=5+(j+i)*10
        mColor=size*1.5
        fill(mColor,20,50)
        ellipse(x,y,size,size)
        fill(250)
        ellipse(x,y,3,3)
    
    

    
