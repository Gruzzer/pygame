import sys, pygame, random

pygame.init()

pygame.display.set_caption("Game")  # Top name

size = width, height = 800, 600
speed = 3
COLOR = 255, 255, 255
score = 0

screan = pygame.display.set_mode(size)

# Time
timelimit = 30
clock = pygame.time.Clock()

# font and text
font = pygame.font.Font("PressStart2P.ttf", 30)
text = font.render(u"SCORE : %d" % score, True, (250, 0, 0))

# MUSIC
pygame.mixer.music.load("8-punk-8-bit-music.mp3")
pygame.mixer.music.play(-1,0.0)    # (재생횟수, n초부터)
pickupsound = pygame.mixer.Sound("Beep8.wav")

# IMAGE load and rect
background = pygame.image.load("BG.jpg")
item1 = pygame.image.load("Apple.png")
item1rect = item1.get_rect()
PAC = pygame.image.load("PAC_R.png")
PACrect = PAC.get_rect()
Gameover = pygame.image.load("gameover.png")
GGrect = Gameover.get_rect()

# spawn x,y
item1rect.left = random.randint(1, 700)
item1rect.top = random.randint(1, 500)
GGrect.left = 50
GGrect.top = 200


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# eat apple event
    if PACrect.colliderect(item1rect):
        pickupsound.play(0, 0)  # (횟수,n초부터)
        score += 1
        text = font.render(u"SCORE : %d" % score, True, (250, 0, 0))
        item1rect.left = random.randint(1, 700)
        item1rect.top = random.randint(1, 500)
# Time limit
    if clock.tick(100):
        timelimit -= 0.01
        text = font.render(u"SCORE : %d TIME : %d" %(score, timelimit), True, (250, 0, 0))
# event pressed key option
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if timelimit % 1 < 0.5:                   # 0.5초마다 캐릭터 이미지 바꿔서 움직이는 것처럼 보이기
            PAC = pygame.image.load("PAC_U.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
        PACrect.top -= speed
    if pressed[pygame.K_DOWN]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_D.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
        PACrect.bottom += speed
    if pressed[pygame.K_LEFT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_L.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
        PACrect.left -= speed
    if pressed[pygame.K_RIGHT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_R.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
        PACrect.right += speed
    if pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_RU.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
    if pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_RD.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
    if pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_LD.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
    if pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
        if timelimit % 1 < 0.5:
            PAC = pygame.image.load("PAC_LU.png")
        else:
            PAC = pygame.image.load("PAC_m2.png")
# Image Lock
    if PACrect.left < 0:
        PACrect.left += speed
    if PACrect.right > width:
        PACrect.right -= speed
    if PACrect.top < 0:
        PACrect.top += speed
    if PACrect.bottom > height:
        PACrect.bottom -= speed
# Time over
    if timelimit<0:
        for i in range(200):
            Gameover = pygame.image.load("gameover.png")
            screan.blit(Gameover, GGrect)
            pygame.display.flip()
            Gameover = pygame.image.load("gameover2.png")
            screan.blit(Gameover, GGrect)
            pygame.display.flip()
        sys.exit()

    screan.fill(COLOR)
    #screan.blit(background, (0, 0))
    screan.blit(PAC, PACrect)
    screan.blit(item1, item1rect)
    screan.blit(text, text.get_rect())
    pygame.display.flip()   # update display
