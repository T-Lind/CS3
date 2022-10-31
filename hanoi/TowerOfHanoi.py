import pygame
from HanoiFiles import TowersOfHanoi
pygame.init()


window = pygame.display.set_mode((576, 576))
image = pygame.image.load(r'temple.jpg')

solver = TowersOfHanoi(10, pygame, window, height=20, action_delay=0)
solver()

input("Press 'Enter' to exit")
