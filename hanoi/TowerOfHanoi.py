import pygame
from HanoiFiles import TowersOfHanoi
pygame.init()


window = pygame.display.set_mode((576, 576))
image = pygame.image.load(r'temple.jpg')

solver = TowersOfHanoi(5, pygame, window, action_delay=0.05)
solver()

input()
