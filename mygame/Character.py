import pygame

class character():
    def __init__(self):
        self.HP = 0
        self.SPD = 0
        self.SHOT_SPD = 0
        self.DMG = 0
        self.Image = pygame.image.load()
        self.I_rect = self.Image.get_rect()

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.I_rect.top -= self.SPD
        if pressed[pygame.K_DOWN]:
            self.I_rect.bottom -= self.SPD
        if pressed[pygame.K_LEFT]:
            self.I_rect.left -= self.SPD
        if pressed[pygame.K_RIGHT]:
            self.I_rect.right -= self.SPD

    def CharacterLock(self, width, height):
        if self.I_rect.left < 0:
            self.I_rect.left += self.SPD
        if self.I_rect.right > width:
            self.I_rect.right -= self.SPD
        if self.I_rect.top < 0:
            self.I_rect.top += self.SPD
        if self.I_rect.bottom > height:
            self.I_rect.bottom -= self.SPD

    def motion(self):
        pass

    def Attack(self):
        pass
