import sys
import pygame
from instellingen import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FrogMan")
screen.fill((0, 0, 255))
clock = pygame.time.Clock()

# all sprites group for camera
all_sprites = pygame.sprite.Group()

# sprite
player = Player(all_sprites, (600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # draw background with no repeating images
    screen.fill((0, 0, 255))

    # update
    all_sprites.update(dt)

    # draw
    all_sprites.draw(screen)

    # update the display
    pygame.display.update()
