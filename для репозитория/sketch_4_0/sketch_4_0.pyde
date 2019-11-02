w=500
h=500
s=100

size(500,500)
smooth()
background(255)
fill(50,80)
stroke(100)
strokeWeight(3)
noLoop()

ellipse(w/2,h/2-s/2,s,s)
ellipse(w/2-s/2,h/2,s,s)
ellipse(w/2+s/2,h/2,s,s)
ellipse(w/2,h/2+s/2,s,s)
