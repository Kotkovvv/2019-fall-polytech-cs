w=50
h=50
gamekey=True
blockW=30
blockH=100
blockS=8
colorL = color(255,0,0)
colorR = color(0,83,138)
scoreL = 0
scoreR = 0
winScore = 3

def setup():
  textSize(30)
  textAlign(CENTER, CENTER);
  rectMode(CENTER)
  size(500, 500)
  global x,y, blockXL, blockYL, blockW, blockH, blockXL,blockXR, blockYR, upL, upR, speedX, speedY
  x = width/2
  y = height/2
  w = 50
  h = 50
  speedX = 1.25
  speedY = 1.25
  blockXL = 40
  blockYL = height/2
  blockXR = width-40
  blockYR = height/2
  blockW = 30
  blockH = 100
  blockS = 5
  
def draw():
  if gamekey:  
    background(0)
    drawCircle()
    moveCircle()
    bounceOff()
    drawblocks()
    restrictblock()
    contactblock()
    scores()
    gameOver()
  gamekeystart()
    
def drawblocks():
  global blockXL, blockYL, blockW, blockH, blockXL, blockXR, blockYR
  fill(colorL)
  rect(blockXL, blockYL, blockW, blockH)
  fill(colorR)
  rect(blockXR, blockYR, blockW, blockH)
  
def restrictblock():
  global blockYL,  blockH, blockYR, blockS
  if blockYL - blockH/2 < 0: 
    blockYL = blockYL + blockS;
  
  if blockYL + blockH/2 > height:
    blockYL = blockYL - blockS;
  
  if blockYR - blockH/2 < 0:
    blockYR = blockYR + blockS;
  
  if blockYR + blockH/2 > height:
    blockYR = blockYR - blockS;
    
def contactblock():
  global speedX
  if x-w/2<blockXL+blockW/2 and y-h/2<blockYL+blockH/2 and y + h/2 > blockYL - blockH/2:
    if speedX<0:
      speedX=-speedX*1;
  if x+w/2>blockXR-blockW/2 and y-h/2<blockYR+blockH/2 and y+h/2>blockYR-blockH/2:
    if speedX > 0:
      speedX = -speedX*1;
      
def drawCircle():
  fill(255,255,255);
  ellipse(x, y, w, h);
  
def moveCircle():  
  global x,y
  x = x + speedX*2;
  y = y + speedY*2;

def bounceOff():
 global scoreR, speedY,speedX, scoreL
 if x > width - w/2:
    setup();
    speedX = -speedX;
    scoreL = scoreL + 1;
 if  x < 0 + w/2:
    setup();
    scoreR = scoreR + 1;
  
 if  y > height - h/2:
    speedY = -speedY;
 if y < 0 + h/2:
    speedY = -speedY;
    
def scores():
  fill(255);
  text(scoreL, 100, 50)
  text(scoreR, width-100, 50)
    
def keyPressed():
    global upL, upR, downR, downL, blockYL, blockS,blockYR
    if key == "w" or key == "W":
        blockYL = blockYL - blockS
    if key == "s" or key == "S":
        blockYL = blockYL + blockS
    if keyCode == UP:
        blockYR = blockYR - blockS
    if keyCode == DOWN:
        blockYR = blockYR + blockS
  
def gameOverPage(winner):
  global speedX,speedY, gamekey
  fill(255)
  text("Game over", width/2, height/3 - 40)
  text("Click mouse to play again", width/2, height/3 + 40)
  text(winner ,width/2,height/3 - 80)
  gamekey= False
    
def gameOver():
  if scoreL == winScore:
    gameOverPage("Red wins!")
  if scoreR == winScore:
    gameOverPage("Blue wins!")
    
def gamekeystart():
    global gamekey,scoreR,scoreL, speedX, speedY,blockXL,blockYL,blockXR,blockYR
    if mousePressed:
        gamekey=True
        scoreR = 0
        scoreL = 0
        speedX = 1.25
        speedX = 1.25
        blockXL = 40
        blockYL = height/2
        blockXR = width-40
        blockYR = height/2
