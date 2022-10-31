import time

import pygame, sys, random, itertools
from pygame.locals import *


class ArkanoidEngine:
    def __init__(self, size=640):
        pygame.init()
        pygame.display.set_caption("Arkanoid")

        self.size = width, height = size, size
        self.screen = pygame.display.set_mode(self.size)

        # Define colors
        self.black = (0, 0, 0)
        self.gray = (100, 100, 100)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        # Create the player
        self.player_width = 100
        self.player_rect = Rect(width / 2, height - 20, self.player_width, 7)
        pygame.draw.rect(self.screen, self.gray, self.player_rect)

        # Create the ball
        self.ball = Rect(width / 2, height - 40, 10, 10)
        self.ball_speed = [1, -1]

        # Create the blocks
        self.blocks = []

        # Variable to slow everything down
        self.last_moved = 0

        # Create a font object
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.create_blocks()

    def move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.player_rect.x > 1 and self.last_moved == 0:
                self.player_rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT] and self.last_moved == 0:
            if self.player_rect.x < self.size[0] - self.player_width - 1:
                self.player_rect.move_ip(1, 0)
        pygame.draw.rect(self.screen, self.gray, self.player_rect)

    def move_ball(self):
        if self.last_moved == 0:
            self.ball.move_ip(self.ball_speed)
            if self.ball.left < 0 or self.ball.right > self.size[0]:
                self.ball_speed[0] = -self.ball_speed[0]
            if self.ball.top < 0 or self.ball.bottom > self.size[1]:
                self.ball_speed[1] = -self.ball_speed[1]
            if self.ball.bottom + 1 == self.size[1] - 20 and \
                    self.player_rect.x < self.ball.x < self.player_rect.x + self.player_width:
                self.ball_speed[1] = -self.ball_speed[1]
            self.last_moved += 1

        else:
            self.last_moved += 1
            if self.last_moved > 5:
                self.last_moved = 0

        pygame.draw.rect(self.screen, self.white, self.ball)

    @staticmethod
    def end_catch():
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def check_loss(self):
        if self.ball.bottom > self.size[1] - 10:
            self.ball_speed = [0, 0]
            loss_text = self.font.render('You Lost!', True, self.red, self.black)
            textRect = loss_text.get_rect()
            textRect.center = (self.size[0] // 2, self.size[1] // 2)
            self.screen.blit(loss_text, textRect)
            self.end_catch()

    def win(self):
        self.ball_speed = [0, 0]
        loss_text = self.font.render('You Win!', True, self.red, self.black)
        textRect = loss_text.get_rect()
        textRect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(loss_text, textRect)
        self.end_catch()

    def create_blocks(self):
        for r in range(10, self.size[1] // 4 + 10, self.size[1] // 4 // 2):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for c in range(0, self.size[0], self.size[0] // 10):
                block = Rect(c, r, 60, 17)
                self.blocks.append((block, color))
                pygame.draw.rect(self.screen, color, block)

    def update_blocks(self):
        for i in itertools.count(0):
            if len(self.blocks) == 0:
                self.win()

            if i >= len(self.blocks):
                break

            if self.ball.top - 2 <= self.blocks[i][0].bottom <= self.ball.top + 2 and self.blocks[i][
                0].left <= self.ball.centerx <= self.blocks[i][0].right:
                self.ball_speed[1] = -self.ball_speed[1]
                del self.blocks[i]
            elif self.blocks[i][0].bottom <= self.ball.centery <= self.blocks[i][0].top and self.ball.left - 2 <= \
                    self.blocks[i].right <= self.ball.left + 2:
                self.ball_speed[0] = -self.ball_speed[0]
            elif self.blocks[i][0].bottom <= self.ball.centery <= self.blocks[i][0].top and self.ball.right - 2 <= \
                    self.blocks[i].left <= self.ball.right + 2:
                self.ball_speed[0] = -self.ball_speed[0]
            else:
                pygame.draw.rect(self.screen, self.blocks[i][1], self.blocks[i][0])

    def __call__(self):
        self.screen.fill(self.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.update_blocks()

        self.move_ball()
        self.move_player()

        self.check_loss()

        pygame.display.update()
