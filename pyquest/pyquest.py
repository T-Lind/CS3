import sys, random
import pygame
from pygame.locals import *
from pygame import mixer
from actors import *
from PyQuestFunctions import Environment, render_text, play_sound

env = Environment()

clock = pygame.time.Clock()

in_game_loop: bool = True
reset: bool = False
level: int = 2

while in_game_loop:
    clock.tick(60)

    # (doing event.get(type), then event.clear() is actually a Bad Thing
    # since more events can be added that get cleared w/o being examined)
    for event in pygame.event.get(pygame.KEYUP):
        if event.key == pygame.K_ESCAPE:
            in_game_loop = False
        if reset and event.key == pygame.K_r:
            n_eneimies: int = 10
            for _ in range(level):
                n_eneimies += n_eneimies // 2
            env.reset_env(n_badguys=n_eneimies)
            reset = False
    env.sprites.update()
    pygame.event.clear()

    for L in sprite.groupcollide(env.player.shots, env.badguy_sprites, True, True).values():
        play_sound('explode.wav')
        for badguy in L:
            for i in range(2):
                velocity = tuple(random.randint(0, 5) - 2 for i in range(2))
                debris = BadGuyDebris(badguy.rect.center, velocity)
                debris.update()
                env.transient_sprites.add(debris)
    if not env.badguy_sprites:
        render_text('Clear!', env.background)
        env.screen.blit(env.background, (0, 0))

    # (could use spritecollide, but then have to special case prota already dead)
    if sprite.groupcollide(env.prota_sprites, env.badguy_sprites, False, False):
        mixer.music.fadeout(1000)
        play_sound('explode.wav')
        chan = play_sound('gameover.wav', 1)
        env.prota_sprites.remove(env.player)
        debris = ProtaDebris(env.player.rect.center, env.player.velocity)
        debris.update()
        env.transient_sprites.add(debris)
    if not env.prota_sprites:
        render_text('Game Over!', env.background)
        render_text('(r) to reset and (ESC) to exit', env.background, font_size=18, y=env.background.get_height() // 12)
        env.screen.blit(env.background, (0, 0))
        reset = True

    env.prepare_screen()

sys.exit(0)
