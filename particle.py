import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
class Particle(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.lifetime=1.5
    def update(self,dt):
        self.position+=self.velocity*dt
        self.lifetime-=dt
        if self.lifetime<=0:
            self.kill()

    def draw(self,screen):
        pygame.draw.circle(screen,"orange",self.position,self.radius,LINE_WIDTH)