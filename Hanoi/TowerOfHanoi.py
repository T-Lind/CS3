import pygame
from Ring import Ring
pygame.init()
pygame.display.set_caption("Tower of Hanoi Solver")

window = pygame.display.set_mode((576, 576))
image = pygame.image.load(r'temple.jpg')


ring1 = Ring(1)
ring2 = Ring(2)
ring3 = Ring(3)
ring4 = Ring(4)
ring5 = Ring(5)
ring6 = Ring(6)
stack = 3
ring1.update(pygame, window, stack=stack)
ring2.update(pygame, window, stack=stack, beneath=1)
ring3.update(pygame, window, stack=stack, beneath=2)
ring4.update(pygame, window, stack=stack, beneath=3)
ring5.update(pygame, window, stack=stack, beneath=4)
ring6.update(pygame, window, stack=stack, beneath=5)

pygame.display.flip()
window.blit(image, (0, 0))
input()



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
