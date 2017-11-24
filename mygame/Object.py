import pygame

class object():
    def __init__(self):
        self.Image = pygame.image.load("rock.png")
        self.I_rect = self.Image.get_rect()
    def collide(self, Charrect):
        pass


Rock = object()
Rock.I_rect.left = 635
Rock.I_rect.top = 390
