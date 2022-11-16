import sys
import time

from pygame.locals import *
from pygame import mixer
from actors import *
from PyQuestFunctions import Environment, render_end_text, play_sound, get_highscore

framerate: int = 60
in_game_loop: bool = True
reset: bool = False

if __name__ == "__main__":
    clock = pygame.time.Clock()
    env = Environment(start_level=1)
    while in_game_loop:
        render_end_text(f"Score: {env.score:3}",
                        env.background,
                        x=11 * env.background.get_width() / 12,
                        y=env.background.get_height() // 14,
                        window=env.window,
                        color=(205, 205, 205),
                        font_size=13)
        render_end_text(f"High Score: {get_highscore(env):3}",
                        env.background,
                        x=11 * env.background.get_width() / 12,
                        y=env.background.get_height() // 10,
                        window=env.window,
                        color=(205, 205, 205),
                        font_size=13)

        clock.tick(framerate)

        # (doing event.get(type), then event.clear() is actually a Bad Thing
        # since more events can be added that get cleared w/o being examined)
        for event in pygame.event.get(pygame.KEYUP):
            if event.key == pygame.K_ESCAPE:
                in_game_loop = False
            if reset and event.key == pygame.K_r:
                env.reset_env()
                reset = False
        env.sprites.update()
        pygame.event.clear()

        for badguy in sprite.groupcollide(env.player.shots, env.badguy_sprites, True, True).values():
            env.score += 10 * env.level
            play_sound('explode.wav')
            for badguy_components in badguy:
                for i in range(2):
                    velocity = tuple(random.randint(0, 5) - 2 for i in range(2))
                    debris = BadGuyDebris(badguy_components.rect.center, velocity)
                    debris.update()
                    env.transient_sprites.add(debris)
        if not env.badguy_sprites:
            render_end_text('Clear!', env.background)
            env.screen.blit(env.background, (0, 0))
            env.inc_level()

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
            render_end_text('Game Over!', env.background)
            render_end_text('(r) to reset and (ESC) to exit', env.background, font_size=18,
                            y=env.background.get_height() // 12)
            env.screen.blit(env.background, (0, 0))
            reset = True

        env.prepare_screen()

    with open("HighScores.pyquest", "a") as file:
        file.write(str(env.score) + "\n")
    sys.exit(0)
