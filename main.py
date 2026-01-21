import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state





def main():
    pygame.init()
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    x = 0
    while x < 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
        clock.tick(60)
        dt = clock.get_time() / 1000.0  # Delta time in seconds.
        
        pygame.display.flip()
        print(f"{dt} seconds have passed since the last frame.")
    

main()
