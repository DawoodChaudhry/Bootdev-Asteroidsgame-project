import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player




def main():
    pygame.init()
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    clock.tick(60)
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update delta time
        dt = clock.get_time() / 1000.0  # Delta time in seconds. 
        
        #Game State Update
        updatable.update(dt)
        for updates in drawable:
            updates.draw(screen)
        
        #Log after update to game state
        log_state() 
        
        #Draw
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        
        print(f"{dt} seconds have passed since the last frame.")
    

main()
