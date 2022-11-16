import random
from collections import deque
import pygame
from pygame import image, sprite, mouse

def sign(i):
    return i < 0 and -1 or 1
def pow(i, j):
    return sign(i) * abs(i) ** j
def absmin(i, j):
    return sign(i) * min(abs(i), j)

def image_load(fname, colorkey=-1):
    img = image.load(fname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0, 0))[:3]
        img.set_colorkey(colorkey)
    return img
    
def image_frames(img, width=None):
    if not width:
        width = img.get_height()
    size = width, img.get_height()
    images = deque()
    origalpha = img.get_alpha()
    origckey = img.get_colorkey()
    img.set_colorkey(None)
    img.set_alpha(None)
    for x in range(0, img.get_width(), width):
        i = pygame.Surface(size)
        i.blit(img, (0, 0), ((x, 0), size))
        if origalpha:
            i.set_colorkey((0,0,0))
        elif origckey:
            i.set_colorkey(origckey)
        images.append(i)
    img.set_alpha(origalpha)
    img.set_colorkey(origckey)
    return images

class Point:
    def __init__(self, coord):
        self.x, self.y = coord
    def magnitude(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    def __mul__(self, rhs):
        return Point((self.x * rhs, self.y * rhs))
    def __neg__(self):
        return Point((-self.x, -self.y))
    def __nonzero__(self):
        return bool(abs(self.x) >= 1 or abs(self.y) >= 1)
    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        raise IndexError()
    def __repr__(self):
        return repr(tuple(self))
    
class AnimatedSprite(sprite.Sprite):
    def __init__(self, position, velocity, imgfile):
        sprite.Sprite.__init__(self)
        self.frames = image_frames(image_load(imgfile))
        self.image = None
        self.rect = self.frames[0].get_rect()
        self.ticks = 0
        self.velocity = Point(velocity)
        self.rect.center = position
    
class ProtaDebris(AnimatedSprite):
    def __init__(self, position, velocity):
        AnimatedSprite.__init__(self, position, velocity, 'explosion.png')
    def update(self):
        if self.ticks % 5 == 0:
            self.image = self.frames.popleft()
            if not self.frames:
                self.groups()[0].remove(self)
        self.ticks += 1
        self.rect.move_ip(tuple(self.velocity))
    
class BadGuyDebris(AnimatedSprite):
    def __init__(self, position, velocity):
        AnimatedSprite.__init__(self, position, velocity, 'debris-bubble.png')
    def update(self):
        if self.ticks % 5 == 0:
            self.image = self.frames.popleft()
            if not self.frames:
                self.groups()[0].remove(self)
        self.ticks += 1
        self.rect.move_ip(tuple(self.velocity))
    
class BadGuy(AnimatedSprite):
    def __init__(self, window, position):
        AnimatedSprite.__init__(self, position, (0, 0), 'fire.png')
        self.window = window
    def update(self):
        if self.ticks % 5 == 0:
            self.image = self.frames.popleft()
            self.frames.append(self.image)
        self.ticks += 1
        self.rect.move_ip(tuple(self.velocity))
        if not self.window.get_rect().contains(self.rect):
            self.rect.clamp_ip(self.window.get_rect())
            self.velocity = -self.velocity
        if not random.randint(0, 60):
            self.velocity.x = absmin(2, self.velocity.x + random.randint(0, 5) - 2)
            self.velocity.y = absmin(2, self.velocity.y + random.randint(0, 5) - 2)
        
class Shot(sprite.Sprite):
    def __init__(self, group, window, position, velocity):
        sprite.Sprite.__init__(self)
        self.window = window
        self.image = image_load('shot.png', None)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.velocity = tuple(velocity)
    def update(self):
        self.rect.move_ip(self.velocity)
        if not self.window.get_rect().colliderect(self.rect):
            self.groups()[0].remove(self)
  
class Prota(sprite.Sprite):
    def __init__(self, window):
        sprite.Sprite.__init__(self)
        self.image = image_load('prota.png')
        self.rect = self.image.get_rect().inflate(-2, -2)
        self.rect.center = tuple(d / 2 for d in window.get_size())
        self.velocity = Point((0, 0))
        self.window = window
        self.shots = sprite.Group()
    def update(self):
        self.maybe_fire()
        self.move()
    def maybe_fire(self):
        if not self.velocity:
            return
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN): 
            if event.button == 1:
                self.shots.add(Shot(self.shots, self.window, self.rect.center, self.velocity * 2))
    def move(self):
        dx, dy = mouse.get_rel()
        self.velocity.x += dx / 5.0
        self.velocity.y += dy / 5.0
        self.rect.move_ip(tuple(self.velocity))
        if not self.window.get_rect().contains(self.rect):
            self.rect.clamp_ip(self.window.get_rect())
            self.velocity = Point((0, 0))
        # somewhere, pygame truncates self.rect to integer coordinates; this makes fractional velocities
        # kinda sucky.  fix: keep internal position Point instead.
