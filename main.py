import pygame
import sys
from constants import  *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # we put things in groups so that we can call them all at once
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,) #extra comma makes a tuple

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if player.collision(obj):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collision(obj):
                    bullet.kill()
                    obj.split()
        # clear what was drawn in previous frame and prepare for the next rendering
        # this goes before the rendering because its assoicated with draw/rendering
        screen.fill("black") 
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit framerate to 60FPS
        dt = (clock.tick(60)/1000)
    
    
if __name__ == "__main__":
    main()
