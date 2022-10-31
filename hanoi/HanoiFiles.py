import random
import time

import pygame.display


class Ring:
    def __init__(self, precedence, size_in_pixels, height=20, horiz_offset=75):
        self.precedence = precedence

        # self.max_size = max_size
        self.height = height

        self.color = (random.randrange(100, 255),
                      random.randrange(100, 255),
                      random.randrange(100, 255))

        # self.

        self.stack = 0

        self.size_in_pixels = size_in_pixels
        self.horiz_offset = horiz_offset

    def update(self, pg, screen, stack=0, beneath=0):
        self.stack = stack
        pg.draw.rect(screen,
                     self.color,  # 100 added to x might need to go away, mult. changed from 150
                     [self.horiz_offset + self.stack * 200 - self.size_in_pixels / 2,
                      576 - beneath * self.height - self.height, self.size_in_pixels, self.height])


class TowersOfHanoi:
    def __init__(self, num_rings, pg, screen, action_delay=0.1, max_size=100, horiz_offset=75):
        self.a = [Ring(
            x,
            max_size * (1 - x / num_rings) + 20,
            horiz_offset=horiz_offset) for x in range(num_rings)]
        self.b = []
        self.c = []

        self.pg = pg
        self.screen = screen

        font = pg.font.Font('freesansbold.ttf', 32)
        self.text = font.render('Tower of Hanoi Solver', True, (255, 255, 255), (100, 100, 100))
        self.textRect = self.text.get_rect()
        self.textRect.center = (576 // 2, 30)


        self.action_delay = action_delay

    def __call__(self):
        self.__tower_of_hanoi_recursive(len(self.a), self.a, self.b, self.c)

    def __tower_of_hanoi_recursive(self, n, a, c, b):
        """
        Solve the problem with the towers of hanoi
        :param n: the number of rings to stack
        :param a: the a stack of rings
        :param c: the c stack of rings
        :param b: the b stack of rings
        :return: the next recursive step of solving the tower of hanoi
        """
        time.sleep(self.action_delay)

        self.screen.fill((100, 100, 100))
        self.screen.blit(self.text, self.textRect)

        for i in range(len(self.a)):
            self.a[i].update(self.pg, self.screen, stack=0, beneath=i)
        for i in range(len(self.b)):
            self.b[i].update(self.pg, self.screen, stack=1, beneath=i)
        for i in range(len(self.c)):
            self.c[i].update(self.pg, self.screen, stack=2, beneath=i)

        self.pg.display.flip()

        if n == 0:
            return
        self.__tower_of_hanoi_recursive(n - 1, a, b, c)
        b.append(a.pop())
        self.__tower_of_hanoi_recursive(n - 1, c, a, b)
