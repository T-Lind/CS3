import pygame
from HanoiFiles import Ring, TowersOfHanoi
pygame.init()
pygame.display.set_caption("Tower of Hanoi Solver")

window = pygame.display.set_mode((576, 576))
image = pygame.image.load(r'temple.jpg')

solver = TowersOfHanoi(3, pygame, window)

solver()

def tower_of_hanoi_recursive(n, a, c, b):
    """
    Solve the problem with the towers of hanoi
    :param n: the number of rings to stack
    :param a: the a stack of rings
    :param c: the c stack of rings
    :param b: the b stack of rings
    :return: the next recursive step of solving the tower of hanoi
    """
    if n == 0:
        return
    tower_of_hanoi_recursive(n - 1, a, b, c)
    b.append(a.pop())
    tower_of_hanoi_recursive(n - 1, c, a, b)


if __name__ == "__main__":
    # Test the towers of hanoi with 5 items
    a, b, c, = [1, 2, 3, 4, 5], [], []
    tower_of_hanoi_recursive(5, a, b, c)
    print(a, b, c)
