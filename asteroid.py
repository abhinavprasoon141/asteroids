from constants import ASTEROID_MIN_RADIUS
import pygame
import random

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            pass
        else:
            random_angle = random.uniform(20,50)
            A1 = Asteroid(self.x,self.y,self.radius-ASTEROID_MIN_RADIUS)
            A2 = Asteroid(self.x,self.y,self.radius-ASTEROID_MIN_RADIUS)
            A1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
            A2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2
