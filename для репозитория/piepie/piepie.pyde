w=50
h=50
gamekey=True
paddleW=30
paddleH=100
paddleS=8
colorL = color(255,0,0);
colorR = color(0,83,138);
scoreL = 0; 
scoreR = 0;
winScore = 3;

def setup(): 
  textSize(30);
  textAlign(CENTER, CENTER); 
  rectMode(CENTER)
  size(500, 500);
  global x,y, paddleXL, paddleYL, paddleW, paddleH, paddleXL,paddleXR, paddleYR, upL, upR, speedX, speedY
  x = width/2; 
  y = height/2;
  w = 50;
  h = 50;
  speedX = 1.25;
  speedY = 1.25;
  paddleXL = 40;
  paddleYL = height/2;
  paddleXR = width-40;
  paddleYR = height/2;
  paddleW = 30;
  paddleH = 100;
  paddleS = 5;
  
def draw():
  if gamekey:  
    background(0);
    drawCircle();
    moveCircle();
    bounceOff();
    drawPaddles();
    restrictPaddle();
    contactPaddle();
    scores();
    gameOver()
  gamekeystart()
    
  
def drawPaddles():
  global paddleXL, paddleYL, paddleW, paddleH, paddleXL, paddleXR, paddleYR
  fill(colorL);
  rect(paddleXL, paddleYL, paddleW, paddleH);
  fill(colorR);
  rect(paddleXR, paddleYR, paddleW, paddleH);
  

    
    
def restrictPaddle():
  global paddleYL,  paddleH, paddleYR, paddleS
  if paddleYL - paddleH/2 < 0: 
    paddleYL = paddleYL + paddleS;
  
  if paddleYL + paddleH/2 > height:
    paddleYL = paddleYL - paddleS;
  
  if paddleYR - paddleH/2 < 0:
    paddleYR = paddleYR + paddleS;
  
  if paddleYR + paddleH/2 > height:
    paddleYR = paddleYR - paddleS;
    
def contactPaddle():
  global speedX
  if x-w/2<paddleXL+paddleW/2 and y-h/2<paddleYL+paddleH/2 and y + h/2 > paddleYL - paddleH/2:
    if speedX<0:
      speedX=-speedX*1;
  if x+w/2>paddleXR-paddleW/2 and y-h/2<paddleYR+paddleH/2 and y+h/2>paddleYR-paddleH/2:
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
    global upL, upR, downR, downL, paddleYL, paddleS,paddleYR
    if key == "w" or key == "W":
        paddleYL = paddleYL - paddleS
    if key == "s" or key == "S":
        paddleYL = paddleYL + paddleS
    if keyCode == UP:
        paddleYR = paddleYR - paddleS
    if keyCode == DOWN:
        paddleYR = paddleYR + paddleS
  
def gameOverPage(winner):
  global speedX,speedY, gamekey
  fill(255)
  text("Game over", width/2, height/3 - 40)
  text("Click to play again", width/2, height/3 + 40)
  text(winner ,width/2,height/3 - 80)
  gamekey= False
    
def gameOver():
  if scoreL == winScore:
    gameOverPage("Red wins!")
  if scoreR == winScore:
    gameOverPage("Blue wins!")
    
def gamekeystart():
    global gamekey,scoreR,scoreL, speedX, speedY,paddleXL,paddleYL,paddleXR,paddleYR
    if mousePressed:
        gamekey=True
        scoreR = 0
        scoreL = 0
        speedX = 1.25
        speedX = 1.25
        paddleXL = 40
        paddleYL = height/2
        paddleXR = width-40
        paddleYR = height/2
