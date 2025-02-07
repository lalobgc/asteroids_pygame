from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.random_angle = random.uniform(20, 50)
        self.splitted_v1 = self.velocity.rotate(self.random_angle)
        self.splitted_v2 = self.velocity.rotate(self.random_angle*(-1))
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_1.velocity = self.splitted_v1 * 1.2
        asteroid_2.velocity = self.splitted_v2 * 1.2
        self.kill()

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
