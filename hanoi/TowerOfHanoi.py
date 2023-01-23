import pygame
from HanoiFiles import TowersOfHanoiSolver
pygame.init()

if __name__ == "__main__":
    # Number of rings to move on the tower of Hanoi
    N_RINGS = 6

    # Time between movements. Larger = slower runtime
    ACTION_DELAY = 0.03

    # Height of each block
    HEIGHT = 30

    # Instantiate the pygame window
    window = pygame.display.set_mode((576, 576))

    # Create the tower of hanoi
    solver = TowersOfHanoiSolver(N_RINGS, pygame, window, height=HEIGHT, action_delay=ACTION_DELAY)

    # Start solving the tower
    solver()

    input("Press 'Enter' to exit")
