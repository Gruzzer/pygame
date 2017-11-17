import sys, pygame

pygame.init()

size = width, height = 800, 600
speed = 1
black = 255,255,255

screan = pygame.display.set_mode(size)

pacman_R= pygame.image.load("pacman1_R.png")
R1rect=pacman_R.get_rect()
pacman_R2= pygame.image.load("pacman2_R.png")
R2rect=pacman_R.get_rect()
pacman_R3= pygame.image.load("pacman3.png")
R3rect=pacman_R.get_rect()
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    def pressed():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            ballrect.top -= speed
        if pressed[pygame.K_DOWN]:
            ballrect.bottom += speed
        if pressed[pygame.K_LEFT]:
            ballrect.left -= speed
        if pressed[pygame.K_RIGHT]:
            ballrect.right += speed
    def protect():
        if ballrect.left < 0:
            ballrect.left+=speed
        if ballrect.right > width:
            ballrect.right-=speed
        if ballrect.top < 0:
            ballrect.top += speed
        if ballrect.bottom > height:
            ballrect.bottom -= speed

    pressed()
    protect()

    screan.fill(black)
    screan.blit(ball,ballrect)
    pygame.display.flip()