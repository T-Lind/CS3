import pygame

from ArkanoidEngine import ArkanoidEngine
clock = pygame.time.Clock()

engine = ArkanoidEngine()
while True:
    clock.tick(1005)
    engine()
