import sys, random
import pygame
from pygame.locals import *
from pygame import display, mixer, font
from pygame.mixer import Channel

from actors import *


class Environment:
    """
    Class that contains all sub-objects as well as other useful functions for the PyQuest
    game environment.
    """

    def __init__(self, start_level=1, scoring="multiply", win_width=800, win_height=600):
        """
        Create the environment
        :param start_level: The level to start at, defaults to 1 but can start at whatever you want
        :param scoring: multiply - multiply level by 10 to add to score, cumulative - just count individual kills as 1 pt
        """
        pygame.init()

        # Level should be set to whatever you want to start at, with no score and either multiply/cumulative scoring
        self.level = start_level
        self.score = 0
        self.scoring_method = scoring

        # Create the objects governing the game
        self.window = display.set_mode((win_width, win_height), pygame.FULLSCREEN)
        display.set_caption('Python Quest')
        self.screen = display.get_surface()
        self.background = pygame.Surface(self.screen.get_size())

        # Create sprites
        self.player = Prota(self.window)
        self.prota_sprites = sprite.Group(self.player)
        self.badguy_sprites = sprite.Group()
        self.transient_sprites = sprite.Group()

        mouse.set_visible(False)

        # Spawn in the enemies

        # Range for spawning enemies
        self.ranges = [i for i in range(0, self.window.get_width() // 4)] \
                      + [i for i in range(3 * self.window.get_width() // 4, self.window.get_width())]

        for i in range(self.__get_n_enemies(self.level)):
            spawnpoint = self._generate_spawnpoint()
            self.badguy_sprites.add(BadGuy(self.window, spawnpoint))
        # We want prota to be drawn last, so put it last in the multigroup
        self.sprites = MultiGroup(self.transient_sprites, self.player.shots, self.badguy_sprites, self.prota_sprites)

        # Determine the high score and store it
        self.highscore = self.read_highscore()

        # Load sounds
        self.explode_sound = mixer.Sound("explode.wav")
        self.gameover_sound = mixer.Sound("gameover.wav")

    def __get_n_enemies(self, level) -> int:
        """
        Given the certain level, calculate how many enemies there should be
        :param level: The level of the game to calculate (1->inf)
        :return: The number of enemies, starts at 10 and adds 50% each time
        """
        n_eneimies: int = 10
        for _ in range(level - 1):
            n_eneimies += n_eneimies // 2
        return n_eneimies

    def prepare_screen(self) -> None:
        """
        Clear the screen and draw the background
        """

        # TODO: Remove try/catch!
        try:
            self.sprites.clear(self.screen, self.background)
            self.sprites.draw(self.screen)
            display.flip()
        except Exception as _:
            pass

    def enemy_killed_score(self) -> None:
        """
        Add a certain amount of score based on the scoring method described when an enemy is killed
        """
        if self.scoring_method == "multiply":
            self.score += self.level * 10
        elif self.scoring_method == "cumulative":
            self.score += 1
        else:
            raise TypeError(f"Invalid scoring type specified: {self.scoring_method}")

    def inc_level(self) -> None:
        """
        Add one to the level, reset the player, and environment
        """
        self.player = Prota(self.window)
        self.level += 1
        self.reset_env()

    def get_highscore(self) -> int:
        """
        Based on previous file data, determine the highest score to date
        """
        return max(self.highscore, self.score)

    def read_highscore(self) -> int:
        """
        Read local file data to determine the highest score
        """
        highscore = 0
        if self.scoring_method == "multiply":
            with open("HighScoresMult.pyquest", "r") as file:
                for line in file.readlines():
                    if int(line) > highscore:
                        highscore = int(line)

        if self.scoring_method == "cumulative":
            with open("HighScoresCum.pyquest", "r") as file:
                for line in file.readlines():
                    if int(line) > highscore:
                        highscore = int(line)
        return highscore

    def save_score(self) -> None:
        """
        Save scores in their respective files, only if the score is nonzero
        """
        if self.scoring_method == "multiply" and self.score != 0:
            with open("HighScoresMult.pyquest", "a") as file:
                file.write(str(self.score) + "\n")
        elif self.scoring_method == "cumulative" and self.score != 0:
            with open("HighScoresCum.pyquest", "a") as file:
                file.write(str(self.score) + "\n")

    def reset_level_score(self) -> None:
        """
        Read the high score to see if anything changed, and then reset the level and score
        """
        self.highscore = self.read_highscore()
        self.level = 1
        self.score = 0

    def reset_env(self, n_badguys=-1) -> None:
        """
        Reset the environment. You can specify a number of enemies,
        otherwise default is to just adhere to what the level says
        :param n_badguys: How many bad guys to spawn, less than 0 = default #
        """
        pygame.init()

        if n_badguys <= 0:
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
            spawnpoint = self._generate_spawnpoint()
            self.badguy_sprites.add(BadGuy(self.window, spawnpoint))
        # we want prota to be drawn last, so put it last in the multigroup
        self.sprites = MultiGroup(self.transient_sprites, self.player.shots, self.badguy_sprites, self.prota_sprites)

    def _generate_spawnpoint(self) -> tuple:
        """
        Create a spawnpoint for enemies from a defined range. Cannot start in middle half of screen width/height
        :param window: the object containing just where the game is on the screen
        :return: a random spawn point
        """
        return random.choice(self.ranges), random.choice(self.ranges)

    def play_sound(self, filename, volume=0.5) -> Channel:
        """
        Play a sound through pygame for effect
        :param filename: the file of the sound to play
        :param volume: the volume at which to play it with
        :return:
        """

        # Either assign gameover or explore sound and play it
        snd = self.gameover_sound if filename == "gameover.wav" else self.explode_sound
        chan = mixer.find_channel(True)
        chan.set_volume(volume)
        chan.play(snd)
        return chan


class MultiGroup:
    """
    A class to hold multiple entities in a list
    """

    def __init__(self, *args):
        self.entity_list = list(args)

    def __getattr__(self, attr):
        def f(*args, **kwargs):
            for group in self.entity_list:
                getattr(group, attr)(*args, **kwargs)

        return f


def render_end_text(
        string_text,
        bkg,
        x=-1,
        y=20,
        color=(200, 10, 10),
        font_size=48,
        window=None) -> None:
    """
    Render some text for display
    :param string_text: The string to display
    :param bkg: the background object to display it on
    :param x: The x coordinate of the text to display. Default is -1 which is then set to half of window size
    :param y: The y coordinate of the text to display. Default is 20.
    :param color: The tuple of color (r, g, b)
    :param font_size: The size in point of font to display
    :param window: The window object to reference, optional but used in case the text should be regularly updated
    """
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
