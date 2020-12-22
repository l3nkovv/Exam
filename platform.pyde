ballX = 300 + int(random(-180,180))
ballY = 100
speedX = 6
speedY= 12
hit = 0
miss = 0
distance = 0
platform = 0

def setup():
    size(600,400)
    frameRate(60)
def draw():
    global ballX, ballY, speedX, speedY, hit, miss, platform, distance
    background(120, 120, 120)
   
    platform = 1000/(hit + 10)
    fill(40,40,40)
    ballX = ballX + speedX
    ballY = ballY + speedY
    rect(mouseX-platform, height-15, 2*platform, 20)
    fill(220,0,0)
    ellipse(ballX, ballY, 25, 25)
    if (ballX < 0) or (ballX > width): speedX = -speedX
    if (ballY > height) or (ballY<0):
        speedY = -speedY
        distance = abs(mouseX - ballX)
        if (distance < platform): hit += 1
        else:
            miss += 1
    else:
        speedY += 1
    
    fill(0)
    textSize(16)
    text("hit:", 5, 15)
    text( hit, 50, 15)
    text("miss:", 5, 30)
    text( miss, 50, 30)

    if (frameCount > 1800):
        textSize(36)
        textAlign(CENTER)
        text("Game over", 310, 205)
        text("Hit:", 300, 240)
        text("Miss:", 300, 280)
        text(miss, 385, 280)
        text(hit, 385, 240)
        delay(1100)
