from circleshape import CircleShape
import pygame,random
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
from particle import Particle

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,) -> None:
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position+=self.velocity*dt
    def split(self) ->int:
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return 20
        log_event("asteroid_split")
        angel = random.uniform(20,50)
        particle_angel = random.uniform(0,100)
        new_vect = self.velocity.rotate(angel)
        new_vect2 = self.velocity.rotate(-angel)
        new_vect_part = self.velocity.rotate(particle_angel)
        new_vect2_part = self.velocity.rotate(-particle_angel)
        new_vect3_part = self.velocity.rotate(particle_angel+30)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        particle_radius=ASTEROID_MIN_RADIUS/2
        new_ast = Asteroid(self.position.x,self.position.y,new_radius)
        new_ast2 = Asteroid(self.position.x,self.position.y,new_radius)
        particle= Particle(self.position.x,self.position.y,particle_radius)
        particle2= Particle(self.position.x,self.position.y,particle_radius)
        particle3= Particle(self.position.x,self.position.y,particle_radius)
        particle.velocity=new_vect_part*1.2
        particle2.velocity=new_vect2_part*1.2
        particle3.velocity=new_vect3_part*1.2
        new_ast.velocity=new_vect*1.2
        new_ast2.velocity=new_vect2*1.2
        return 10