import pygame
import sys
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main():
    pygame.init()
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    clock.tick(60)
    dt = 0
    
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Containers 
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    #Game Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
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
        for asteroid in asteroids:
            if player.collides_width(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        #Log after update to game state
        log_state() 
        
        #Draw
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
              
        pygame.display.flip()
        
        
        print(f"{dt} seconds have passed since the last frame.")
    

main()
