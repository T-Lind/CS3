import pygame

from ArkanoidEngine import ArkanoidEngine

if __name__ == "__main__":
    clock = pygame.time.Clock()
    clock.tick(100)
    engine = ArkanoidEngine()
    while True:
        engine()
