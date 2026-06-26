from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS,LINE_WIDTH
from logger import log_state,log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
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
    shots = pygame.sprite.Group()
    Shot.containers =(updatable,drawable,shots)
    Player.containers = (updatable,drawable)
    Asteroid.containers =(updatable,drawable,asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    score = 0
    font = pygame.font.SysFont(None,36)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        screen.fill("black")
        score_text = font.render(f"Score : {score}",True,"white")
        screen.blit(score_text,(10,10))
        for elem in drawable:
            elem.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for sh in shots:
                if ast.collides_with(sh):
                    log_event("asteroid_shot")
                    score+=ast.split()
                    sh.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
