import sys, random
import pygame
from pygame.locals import *
from pygame import image, display, mouse, sprite, mixer, font
from actors import *

class Environment:
    def __init__(self, n_badguys=10):
        pygame.init()

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

    def prepare_screen(self):
        try:
            self.sprites.clear(self.screen, self.background)
            self.sprites.draw(self.screen)
            display.flip()
        except Exception as _:
            pass

    def reset_env(self, n_badguys=10):
        pygame.init()

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


def render_text(
        s,
        bkg,
        x=-1,
        y=20,
        color=(200, 10, 10),
        font_size=48
):
    if x == -1: x = bkg.get_width() // 2

    text = font.Font(None, font_size).render(s, True, color)
    textpos = text.get_rect(centerx=x, centery=y)
    bkg.blit(text, textpos)