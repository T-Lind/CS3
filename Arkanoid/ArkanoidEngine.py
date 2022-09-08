import pygame, sys
from pygame.locals import *

class ArkanoidEngine:
    def __init__(self, difficulty="Normal", size=640):
        pygame.init()
        pygame.display.set_caption("Arkanoid")

        self.difficulty = difficulty

        self.size = width, height = size, size
        self.screen = pygame.display.set_mode(self.size)

        self.black = (0, 0, 0)
        self.gray = (100, 100, 100)
        self.white = (255, 255, 255)

        self.player_width = 100
        self.player_rect = Rect(width/2, height-20, self.player_width, 7)
        pygame.draw.rect(self.screen, self.gray, self.player_rect)

        self.ball = Rect(width/2, height-30, 10, 10)

        self.ball_speed = [1, -1]

        self.last_moved = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.player_rect.x > 1 and self.last_moved == 0:
                self.player_rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT] and self.last_moved == 0:
            if self.player_rect.x < self.size[0]-self.player_width-1:
                self.player_rect.move_ip(1, 0)


    def draw(self):
        pygame.draw.rect(self.screen, self.gray, self.player_rect)


    def move_ball(self):
        if self.last_moved == 0:
            self.ball.move_ip(self.ball_speed)
            if self.ball.left < 0 or self.ball.right > self.size[0]:
                self.ball_speed[0] = -self.ball_speed[0]
            if self.ball.top < 0 or self.ball.bottom > self.size[1]:
                self.ball_speed[1] = -self.ball_speed[1]
            self.last_moved += 1
        else:
            self.last_moved += 1
            if self.last_moved > 5:
                self.last_moved = 0

        pygame.draw.rect(self.screen, self.white, self.ball)

    def run(self):
        self.screen.fill(self.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.draw()
        self.move_ball()
        self.handle_keys()
        pygame.display.update()

