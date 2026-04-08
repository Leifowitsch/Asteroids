import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from player import *
from logger import log_state
from logger import log_event
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
