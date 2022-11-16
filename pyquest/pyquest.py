import sys, random
import pygame
from pygame.locals import *
from pygame import image, display, mouse, sprite, mixer, font
from actors import *


class MultiGroup:
    def __init__(self, *args):
        self.L = list(args)

    def __getattr__(self, attr):
        def f(*args, **kwargs):
            for group in self.L:
                getattr(group, attr)(*args, **kwargs)

        return f


background, window, screen, p, prota_sprites, badguy_sprites, transient_sprites, spawnpoint, sprites = (None,) * 9
def reset_env():
    global background, window, screen, p, prota_sprites, badguy_sprites, transient_sprites, spawnpoint, sprites
    pygame.init()

    window = display.set_mode((800, 600), pygame.FULLSCREEN)
    display.set_caption('Python Quest')
    screen = display.get_surface()
    mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    p = Prota(window)
    prota_sprites = sprite.Group(p)
    badguy_sprites = sprite.Group()
    transient_sprites = sprite.Group()
    for i in range(10):
        spawnpoint = tuple(random.randint(0, dimension) for dimension in screen.get_size())
        badguy_sprites.add(BadGuy(window, spawnpoint))
    # we want prota to be drawn last, so put it last in the multigroup
    sprites = MultiGroup(transient_sprites, p.shots, badguy_sprites, prota_sprites)


reset_env()


def play_sound(filename, volume=0.5):
    # you'd want to cache these in a real app...
    snd = mixer.Sound(filename)
    chan = mixer.find_channel(True)
    chan.set_volume(volume)
    chan.play(snd)
    return chan


def render_bg(s):
    text = font.Font(None, 36).render(s, True, (10, 10, 200))
    textpos = text.get_rect(centerx=background.get_width() / 2)
    background.blit(text, textpos)


clock = pygame.time.Clock()

reset: bool = False
while True:
    clock.tick(60)

    # (doing event.get(type), then event.clear() is actually a Bad Thing
    # since more events can be added that get cleared w/o being examined)
    for event in pygame.event.get(pygame.KEYUP):
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)
        if reset and event.key == pygame.K_r:
            reset_env()
            reset = False
    sprites.update()
    pygame.event.clear()

    for L in sprite.groupcollide(p.shots, badguy_sprites, True, True).values():
        play_sound('explode.wav')
        for badguy in L:
            for i in range(2):
                velocity = tuple(random.randint(0, 5) - 2 for i in range(2))
                debris = BadGuyDebris(badguy.rect.center, velocity)
                debris.update()
                transient_sprites.add(debris)
    if not badguy_sprites:
        render_bg('Clear!')
        screen.blit(background, (0, 0))

    # (could use spritecollide, but then have to special case prota already dead)
    if sprite.groupcollide(prota_sprites, badguy_sprites, False, False):
        mixer.music.fadeout(1000)
        play_sound('explode.wav')
        chan = play_sound('gameover.wav', 1)
        prota_sprites.remove(p)
        debris = ProtaDebris(p.rect.center, p.velocity)
        debris.update()
        transient_sprites.add(debris)
    if not prota_sprites:
        render_bg('Game Over! (r) to reset and (ESC) to exit')
        screen.blit(background, (0, 0))
        reset = True

    try:
        sprites.clear(screen, background)
        sprites.draw(screen)
        display.flip()
    except Exception as e:
        pass
