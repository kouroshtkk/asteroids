import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_SPEED
, PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS)
from shot import Shot
class Player(CircleShape):
    def __init__(self,x:float,y:float):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.cooldown=0
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen:pygame.Surface):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
    def rotate(self,dt:float):
        self.rotation += PLAYER_TURN_SPEED*dt
    def update(self, dt: float,score:int) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown-=dt
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt,score)
        if keys[pygame.K_s]:
            self.move(-dt,score)
        if keys[pygame.K_SPACE]:
            if not self.cooldown>0:
                added_score=score/10000*2
                if score>1000:
                    added_score=0.2
                self.cooldown=PLAYER_SHOOT_COOLDOWN_SECONDS-added_score
                self.shoot(score)
    def move(self,dt:float,score:int):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector=unit_vector.rotate(self.rotation)
        added_score=score
        if score>1000:
            added_score=100
        elif score<-1000:
            added_score=100
        rotated_with_speed_vector = rotated_vector * ((PLAYER_SPEED + added_score/10) * dt)
        self.position+=rotated_with_speed_vector

    def shoot(self,score):
        shot = Shot(self.position.x,self.position.y)
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed = rotated_vector * (PLAYER_SHOOT_SPEED + score//2)
        shot.velocity=rotated_with_speed