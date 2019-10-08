ww=500
wh=500
ws=200
es=100
ew=200
eh=300


size(500,500)
smooth()
background(255)
fill(50,80)
stroke(100)
strokeWeight(3)
noLoop()

ellipse(ww/2,wh/2-es/2,ew,eh)
ellipse(ww/2-es/2,wh/2,ew,eh)
ellipse(ww/2+es/2,wh/2,ew,eh)
ellipse(ww/2,wh/2+es/2,ew,eh)
