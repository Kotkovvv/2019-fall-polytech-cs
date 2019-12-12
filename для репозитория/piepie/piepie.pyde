#int creates variables
#boolean creates false/true option
#color sets color for item
 
x=500/2
y=500/2
w=50
h=50
speedX=4
speedY=4
paddleXL=40
paddleYL=500/2;
paddleW=30
paddleH=100
paddleS=5
paddleXR=500-40
paddleYR= 500/2
upL=0
downL=0
upR=0
downR=0
#colorL and colorR are not needed, but it can be helpful
colorL = color(255,0,0);
colorR = color(0, 255, 0, 50);
#scoreL is for left score and scoreR is for the right score
scoreL = 0; 
scoreR = 0;
#this sets the final winScore to a count of 10
winScore = 10;
 
#Sets the game and window size up, along with the background and other important things
#happens only once; at the beginning of the game
 
def setup(): 
  #this sets the window size
  size(500, 500);
  #the x,y,w,h get the ball to begin at the center of the game
  x = width/2; 
  y = height/2;
  w = 50;
  h = 50;
  #this allows the ball to bounce
  speedX = 4;
  speedY = 4;
  #this creates a text
  textSize(30);
  textAlign(CENTER, CENTER); #this centers the height and width of the text
  rectMode(CENTER); #this allows both paddles to be centered
  #This sets the paddles to a certain place on the window, and makes them visible
  paddleXL = 40;
  paddleYL = height/2;
  paddleXR = width-40;
  paddleYR = height/2;
  paddleW = 30;
  paddleH = 100;
  paddleS = 5;

 
#Draws the canvas for the game
 
def draw():
  background(0);
  drawCircle();
  moveCircle();
  bounceOff();
  drawPaddles();
  movePaddle();
  restrictPaddle();
  contactPaddle();
  scores();
  gameOver();

 
#creates paddles
 
def drawPaddles():
  fill(colorL);
  rect(paddleXL, paddleYL, paddleW, paddleH);
  fill(colorR);
  rect(paddleXR, paddleYR, paddleW, paddleH);

 
#Makes both paddles move
 
def movePaddle():
  if upL:
    paddleYL = paddleYL - paddleS;
  
  if downL:
    paddleYL = paddleYL + paddleS;
  
  if upR:
    paddleYR = paddleYR - paddleS;
  
  if downR:
    paddleYR = paddleYR + paddleS;
  

 
#detects when a paddle has hit the wall
 
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
  

 
#This detects left and right collision; respectively
 
def contactPaddle():
  global speedX
  if x-w/2<paddleXL+paddleW/2 and y-h/2<paddleYL+paddleH/2 and y + h/2 > paddleYL - paddleH/2:
    if speedX<0:
      speedX=-speedX*1;
  if x+w/2>paddleXR-paddleW/2 and y-h/2<paddleYR+paddleH/2 and y+h/2>paddleYR-paddleH/2:
    if speedX > 0:
      speedX = -speedX*1;
    
  

 
#creates circle
def drawCircle():
  fill(0,0,255);
  ellipse(x, y, w, h);

#this allows the circle to bounce
def moveCircle():  
  global x,y
  x = x + speedX*2;
  y = y + speedY*2;

 
#This detects if the ball has bounced or not
 
def bounceOff():
 global scoreR, speedY,speedX, scoreL, scoreR
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
  

 
#This provides the user to see the score
 
def scores():
  fill(255);
  text(scoreL, 100, 50);
  text(scoreR, width-100, 50);

 
#This determines who wins
 
def gameOver():
  if scoreL == winScore:
    gameOverPage("Red wins!", colorL);
  
  if scoreR == winScore:
    gameOverPage("Dark-Green wins!", colorR);
  

 
#This stops the ball from bouncing around, gets the user to know that the game is over
 
def gameOverPage(text, c):
  speedX = 0;
  speedY = 0;
  fill(255);
  print("Game over", width/2, height/3 - 40);
  print("Click to play again", width/2, height/3 + 40);
  fill(c);
  #text(text, width/2, height/3); возможно не пригодится
  #this gets the user to click on the screen to play again
  if mousePressed:
  #this sets the score to zero
    scoreR = 0;
    scoreL = 0;
    #this gets the speed to a 1
    speedX = 1;
    speedY = 1;
  
 
#this gets the user to press a key and allow the paddle(s) to move
 
def keyPressed():
    if key == "w" or key == "W":
        upL = true;
  
    if key == "s" or key == "S":
        downL = true;
  
    if keyCode == UP:
        upR = true;
  
    if keyCode == DOWN:
        downR = true;
  

 
#this creates a false key interaction
 
def keyReleased():
  if key == "w" or key == "W":
    upL = false;
  
  if key == "s" or key == "S":
    downL = false;
  
  if keyCode == UP:
    upR = false;
  
  if keyCode == DOWN:
    downR = false;
  
