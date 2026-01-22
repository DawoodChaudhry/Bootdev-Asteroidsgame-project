import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        random_vector = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        vel = self.velocity.rotate(random_vector) * 1.2
        vel2 = self.velocity.rotate(-random_vector) * 1.2
        asteroid1.velocity = vel
        asteroid2.velocity = vel2
        
        
        
            
        
        
        