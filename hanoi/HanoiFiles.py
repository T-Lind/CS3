import random
import time


class Ring:
    """
    Object for each block in the tower of Hanoi
    """
    def __init__(self, precedence, size_in_pixels, height=20, horiz_offset=75, min_color=100, max_color=255,
                 stack_spacing=200, window_size=576):
        self.precedence = precedence

        # self.max_size = max_size
        self.height = height

        self.color = (random.randrange(min_color, max_color),
                      random.randrange(min_color, max_color),
                      random.randrange(min_color, max_color))

        # self.

        self.stack = 0

        self.size_in_pixels = size_in_pixels
        self.horiz_offset = horiz_offset
        self.stack_spacing = stack_spacing
        self.window_size = window_size

    def update(self, pg, screen, stack=0, beneath=0) -> None:
        """
        Move this ring object
        :param pg: the pygame object
        :param screen: the instantiated screen object from Pygame
        :param stack: the stack that the current ring is in
        :param beneath: number of rings beneath the current. used for y axis alignment
        """
        self.stack = stack
        pg.draw.rect(screen,
                     self.color,  # 100 added to x might need to go away, mult. changed from 150
                     [self.horiz_offset + self.stack * self.stack_spacing - self.size_in_pixels / 2,
                      self.window_size - beneath * self.height - self.height, self.size_in_pixels, self.height])


class TowersOfHanoi:
    """
    A graphical object representing the TowersOfHanoi game.
    """

    def __init__(self, num_rings, pg, screen, action_delay=0.1, max_size=100, min_size=20, height=20, horiz_offset=75,
                 window_size=576, stack_spacing=200, min_color=100, max_color=255, font_type='freesansbold.ttf'):
        self.a = [Ring(
            x,
            max_size * (1 - x / num_rings) + min_size,
            horiz_offset=horiz_offset, stack_spacing=stack_spacing, min_color=min_color,
            max_color=max_color, height=height)
            for x in range(num_rings)]
        self.b = []
        self.c = []

        self.pg = pg
        self.screen = screen

        font = pg.font.Font(font_type, 32)
        self.text = font.render('Tower of Hanoi Solver', True, (255, 255, 255), (100, 100, 100))
        self.textRect = self.text.get_rect()
        self.textRect.center = (window_size // 2, 30)

        self.action_delay = action_delay

        self.num_steps = 0

    def __call__(self):
        self.num_steps = 0
        before_time = time.time()
        self.__tower_of_hanoi_recursive(len(self.a), self.a, self.b, self.c)
        after_time = time.time()
        print(f"Time to solve: {after_time - before_time} seconds.")
        print(f"Steps to solve: {self.num_steps} steps.")

    def __tower_of_hanoi_recursive(self, n, a, c, b) -> None:
        """
        Solve the problem with the towers of hanoi
        :param n: the number of rings to stack
        :param a: the a stack of rings
        :param c: the c stack of rings
        :param b: the b stack of rings
        :return: the next recursive step of solving the tower of hanoi
        """
        time.sleep(self.action_delay)

        self.num_steps += 1

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
