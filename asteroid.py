from circleshape import CircleShape
import pygame,random
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,) -> None:
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angel = random.uniform(20,50)
        new_vect = self.velocity.rotate(angel)
        new_vect2 = self.velocity.rotate(-angel)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast = Asteroid(self.position.x,self.position.y,new_radius)
        new_ast2 = Asteroid(self.position.x,self.position.y,new_radius)
        new_ast.velocity=new_vect*1.2
        new_ast2.velocity=new_vect2*1.2