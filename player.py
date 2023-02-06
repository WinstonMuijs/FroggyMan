import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.index = 0
        # self.animation =
        self.import_frogman()
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def import_frogman(self):
        path = "./graphics/player/right/"
        self.animation = [pygame.image.load(f'{path}{frogman}.png').convert_alpha() for frogman in range(4)]
        # return self.animation

        # animations
        self.animations = {}
        for index, folder in enumerate(walk("./graphics/player")):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in folder[2]:
                    path = folder[0] + '/' + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('/')[-1]
                    self.animations[key].append(surf)
        return self.animations


    def movement(self, dt):
        # normalize the length vector for diagonal direction speed
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def animation_player(self, dt):
        self.index += 10 * dt
        if self.index < len(self.animation):
            self.image = self.animation[int(self.index)]
        else:
            self.index = 0

    def keyboard_input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.animation_player(dt)
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.image.load("./graphics/player/left/0.png")
        else:
            self.direction.x = 0
            # if self.rect.x > WINDOW_WIDTH - 48:
            #     self.rect.x = WINDOW_WIDTH - 48

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.image = pygame.image.load("./graphics/player/up/0.png")
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.image = pygame.image.load("./graphics/player/down/0.png")
        else:
            self.direction.y = 0

            # if self.rect.y > WINDOW_HEIGHT - 64:
            #     self.rect.y = WINDOW_HEIGHT - 64

    def update(self, dt):
        self.animation_player(dt)
        self.keyboard_input(dt)
        self.movement(dt)
