import pygame
from HanoiFiles import TowersOfHanoi
pygame.init()

if __name__ == "__main__":
    window = pygame.display.set_mode((576, 576))

    solver = TowersOfHanoi(6, pygame, window, height=40, action_delay=0.1)
    solver()

    input("Press 'Enter' to exit")
