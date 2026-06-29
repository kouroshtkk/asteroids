from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS,LINE_WIDTH
from logger import log_state,log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from particle import Particle
import pygame
import sys
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    particles = pygame.sprite.Group()

    field_updatable=pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Particle.containers=(updatable,drawable)
    Shot.containers =(updatable,drawable,shots)
    Player.containers = (drawable,field_updatable)
    Asteroid.containers =(updatable,drawable,asteroids)
    AsteroidField.containers = field_updatable
    asteroid_field = AsteroidField()
    score = 0
    font = pygame.font.SysFont(None,36)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0.0
    GAME_STATE = "PLAYING"
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        if GAME_STATE =="PLAYING":
            updatable.update(dt)
            field_updatable.update(dt,score)
            for ast in asteroids:
                if ast.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    GAME_STATE="GAME_OVER"
                for sh in shots:
                    if ast.collides_with(sh):
                        log_event("asteroid_shot")
                        score+=ast.split()
                        sh.kill()
        elif GAME_STATE =="GAME_OVER":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                updatable.empty()
                field_updatable.empty()
                asteroids.empty()
                drawable.empty()
                shots.empty()
                player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                asteroid_field = AsteroidField()
                score=0
                GAME_STATE ="PLAYING"
        screen.fill("black")
        score_text = font.render(f"Score : {score}",True,"white")
        screen.blit(score_text,(10,10))
        for elem in drawable:
            elem.draw(screen)
        if GAME_STATE == "GAME_OVER":
            game_over_text = font.render(f"Game over with {score}",True,"white")
            screen.blit(game_over_text,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2))

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
