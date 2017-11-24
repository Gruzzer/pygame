import pygame, sys
from mygame.Map import *
from mygame.Character import *
from mygame.Object import *

pygame.init()
i = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    Char.move(width, height)
    ZB.Follow(Char.I_rect.x, Char.I_rect.y)
    print(Char.I_rect)
    if i == 0:
        if Char.I_rect.collidepoint(485, 340):
            i += 1
            Char.I_rect.left = 440
            Char.I_rect.top = 500
    if i == 1:
        if Char.I_rect.collidepoint(460, 640):
            i -= 1
            Char.I_rect.left = 450
            Char.I_rect.top = 400



    screan.fill(COLOR)
    screan.blit(Map[i], (0, 0))
    if i == 1:
        screan.blit(Rock.Image, Rock.I_rect)
    screan.blit(Char.Image, Char.I_rect)
    screan.blit(ZB.Image, ZB.I_rect)
    pygame.display.flip()
