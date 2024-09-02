import pygame
import sys

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    you = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(you):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()