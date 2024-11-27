import pygame
from constants import  *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # we put things in groups so that we can call them all at once
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updateable:
            i.update(dt)
        # clear what was drawn in previous frame and prepare for the next rendering
        # this goes before the rendering because its assoicated with draw/rendering
        screen.fill("black") 
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        
        dt = (clock.tick(60)/1000)
    
    


if __name__ == "__main__":
    main()
