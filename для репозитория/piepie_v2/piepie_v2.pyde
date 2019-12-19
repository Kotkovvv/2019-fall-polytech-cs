h=10
gamekey=True
blockW=15
blockH=300
colorL = color(255,0,0)
colorR = color(0,83,138)
score = 0
loseScore=-5
winScore = 5

def setup():
  fullScreen()
  textSize(30)
  textAlign(CENTER, CENTER);
  rectMode(CENTER)
  size(500, 500)
  global x,y, blockXL, blockYL, blockW, blockH, blockXL,blockXR, blockYR, upL, upR, speedX, speedY
  x = width/2
  y = height/2
  speedX = random(9,12)
  speedY = random(5,6)
  blockXL = 40
  blockYL = mouseY
  blockXR = width-40
  blockYR = mouseY
  score=0
  
def draw():
  if gamekey:  
    background(0)
    drawCircle()
    moveCircle()
    bounceOff()
    drawblocks()
    contactblock()
    scores()
    gameOver()
  gamekeystart()
    
    #отрисовка панелей
def drawblocks():
  global blockXL, blockYL, blockW, blockH, blockXL, blockXR, blockYR
  blockYL = mouseY
  blockYR = mouseY
  fill(colorL)
  rect(blockXL, blockYL, blockW, blockH)
  fill(colorR)
  rect(blockXR, blockYR, blockW, blockH)
    
def contactblock():
  global speedX, speedY, score
  if x-h/2<blockXL+blockW/2 and y-h/2<blockYL+blockH/2 and y + h/2 > blockYL - blockH/2:
    if speedX<0:
      speedX=-speedX*1;
      speedX*=random(0.8,1.2)
      speedY*=random(0.9,1.3)
      score=score+1
  if x+h/2>blockXR-blockW/2 and y-h/2<blockYR+blockH/2 and y+h/2>blockYR-blockH/2:
    if speedX > 0:
      speedX = -speedX*1;
      speedX*=random(0.8,1.2)
      speedY*=random(0.9,1.3)
      score=score+1
      
def drawCircle():
  fill(255,255,255);
  ellipse(x, y, h, h);
  
def moveCircle():  
  global x,y
  x = x + speedX*2;
  y = y + speedY*2;

#вылет
def bounceOff():
 global score, speedY,speedX
 if x > width - h/2:
    setup();
    speedX = -speedX;
    score = score - 1;
 if  x < 0 + h/2:
    setup();
    score = score - 1;
  
 if  y > height - h/2:
    speedY = -speedY;
 if y < 0 + h/2:
    speedY = -speedY;
    
def scores():
  fill(255);
  text(score, width/2, 50)

def gameOverPage(winner):
  global speedX,speedY, gamekey
  fill(255)
  text("Your score is", width/2, height/3 -120)
  text("Game over", width/2, height/3 - 40)
  text("Click mouse to play again", width/2, height/3 + 40)
  text(winner ,width/2,height/3 - 80)
  gamekey= False
    
def gameOver():
  if score == winScore or score ==loseScore:
    gameOverPage(score)
    
def gamekeystart():
    global gamekey, speedX, speedY,blockXL,blockYL,blockXR,blockYR,score
    if mousePressed:
        gamekey=True
        score = 0
        speedX = random(9,12)
        speedY = random(5,6)
        blockXL = 40
        blockXR = width-40
        blockYL = mouseY
        blockYR = mouseY
    
def keyPressed():
    global upL, upR, downR, downL, blockYL, blockS,blockYR
    println(keyCode)
    if keyCode in (16,81):
        gameOverPage(score)
