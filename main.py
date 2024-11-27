import pygame
from constants import  *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

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

    Player.containers = (updatable, drawable)
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
