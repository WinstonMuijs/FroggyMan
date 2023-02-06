import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.status = 'right'
        self.index = 0
        self.animations = self.import_frogman()
        self.image = self.animations[self.status][self.index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def import_frogman(self):

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
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.index += 10 * dt
            if self.index >= len(current_animation):
                self.index = 0

        else:
            self.index = 0
        self.image = current_animation[self.index]

    def keyboard_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.status = 'right'
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.status = "left"
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.status = "up"
            self.direction.y = -1

        elif keys[pygame.K_DOWN]:
            self.status = 'down'
            self.direction.y = 1

        else:
            self.direction.y = 0

    def update(self, dt):
        self.animation_player(dt)
        self.keyboard_input()
        self.movement(dt)
