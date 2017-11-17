"""
	 # This is a get_ticks() function simple example
	 # This script should return 10 as a result
"""
# Standard library imports
import time
# Related third party imports
import pygame
#Pygame start function
i=60
pygame.init()
# Create the clock
clock = pygame.time.Clock()
while 1:
    if clock.tick(10):
        i-=1
        print(i)

# Print the seconds
# print(int(round(pygame.time.get_ticks()/1000)))