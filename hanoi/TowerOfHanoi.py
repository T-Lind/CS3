import pygame
from HanoiFiles import TowersOfHanoi
pygame.init()


window = pygame.display.set_mode((576, 576))

solver = TowersOfHanoi(10, pygame, window, height=40, action_delay=0)
solver()

input("Press 'Enter' to exit")
