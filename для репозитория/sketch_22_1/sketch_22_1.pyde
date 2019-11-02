size(500,500)
smooth()
background(255)
strokeWeight(30)
noLoop()
noStroke()

i = 0
k = 0

while k < 10:
    while i < 10:
        if k == 1 or k == 3 or k == 5 or k == 7 or k == 9:
            fill(220 -i*20)
            rect(i*40 + 50, 50 + 40*k, 35, 35)
        else:
            fill(i*20)
            rect(i*40 + 50, 50 + 40*k, 35, 35)
        i +=1
    k += 1
    i = 0
    
