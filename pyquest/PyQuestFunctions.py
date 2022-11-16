import sys, random
import pygame
from pygame.locals import *
from pygame import display, mixer, font
from actors import *


def _generate_spawnpoint(screen):
    spawnpoint = tuple(random.randint(0, dimension) for dimension in screen.get_size())
    while screen.get_size()[0]/4 < spawnpoint[0] < 3*screen.get_size()[0]/4 and \
            screen.get_size()[1] / 4 < spawnpoint[1] < 3 * screen.get_size()[1] / 4:
        spawnpoint = tuple(random.randint(0, dimension) for dimension in screen.get_size())
    return spawnpoint

class Environment:
    def __init__(self, start_level=1):
        pygame.init()

        self.level = start_level
        self.score = 0

        self.window = display.set_mode((800, 600), pygame.FULLSCREEN)
        display.set_caption('Python Quest')
        self.screen = display.get_surface()
        mouse.set_visible(False)

        self.background = pygame.Surface(self.screen.get_size())
        self.player = Prota(self.window)
        self.prota_sprites = sprite.Group(self.player)
        self.badguy_sprites = sprite.Group()
        self.transient_sprites = sprite.Group()

        # Spawn in the enemies
        for i in range(self.__get_n_enemies(self.level)):
            spawnpoint = _generate_spawnpoint(self.screen)

            self.badguy_sprites.add(BadGuy(self.window, spawnpoint))
        # we want prota to be drawn last, so put it last in the multigroup
        self.sprites = MultiGroup(self.transient_sprites, self.player.shots, self.badguy_sprites, self.prota_sprites)

    def __get_n_enemies(self, level):
        n_eneimies: int = 10
        for _ in range(level):
            n_eneimies += n_eneimies // 2
        return n_eneimies

    def prepare_screen(self):
        try:
            self.sprites.clear(self.screen, self.background)
            self.sprites.draw(self.screen)
            display.flip()
        except Exception as _:
            pass

    def reset_env(self, n_badguys=-1):
        pygame.init()

        if n_badguys == -1:
            n_badguys = self.__get_n_enemies(self.level)

        self.window = display.set_mode((800, 600), pygame.FULLSCREEN)
        display.set_caption('Python Quest')
        self.screen = display.get_surface()
        mouse.set_visible(False)

        self.background = pygame.Surface(self.screen.get_size())
        self.player = Prota(self.window)
        self.prota_sprites = sprite.Group(self.player)
        self.badguy_sprites = sprite.Group()
        self.transient_sprites = sprite.Group()
        for i in range(n_badguys):
            spawnpoint = tuple(random.randint(0, dimension) for dimension in self.screen.get_size())
            self.badguy_sprites.add(BadGuy(self.window, spawnpoint))
        # we want prota to be drawn last, so put it last in the multigroup
        self.sprites = MultiGroup(self.transient_sprites, self.player.shots, self.badguy_sprites, self.prota_sprites)


class MultiGroup:
    def __init__(self, *args):
        self.L = list(args)

    def __getattr__(self, attr):
        def f(*args, **kwargs):
            for group in self.L:
                getattr(group, attr)(*args, **kwargs)

        return f


def play_sound(filename, volume=0.5):
    # you'd want to cache these in a real app...
    snd = mixer.Sound(filename)
    chan = mixer.find_channel(True)
    chan.set_volume(volume)
    chan.play(snd)
    return chan


def render_end_text(
        string_text,
        bkg,
        x=-1,
        y=20,
        color=(200, 10, 10),
        font_size=48,
        window=None
):
    if x == -1: x = bkg.get_width() // 2

    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(string_text, True, color, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (x, y)

    # text = font.Font(None, font_size).render(string_text, True, color)
    # textRect = text.get_rect()
    bkg.blit(text, textRect)
    if window is not None:
        window.blit(text, textRect)
