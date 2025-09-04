import pygame

from .models.sprite import MySprite
from .models.car import Car

def main():
    pygame.init()

    # Variables and constants
    FPS = 30
    screen = pygame.display.set_mode((1280, 720))
    pos_x, pos_y = pygame.display.get_window_size()
    car_sprite = MySprite("src/assets/img/car1.png", 50, pos_y - 200)

    car1 = Car(car_sprite, 100, (pos_x, pos_y))

    clock = pygame.time.Clock()

    running = True
    while running:        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYUP:
                # The car up (axis y)
                if ev.key == pygame.K_UP:
                    car1.up()
                    # Re-draw to update
                    car1.draw(screen)
                # The car down (axis y)
                elif ev.key == pygame.K_DOWN:
                    car1.down()
                    car1.draw(screen)
        
        screen.fill((55, 255, 0))

        # Backroung image
        # After will be replaced with the "Road" model|object
        screen.blit(pygame.image.load("src/assets/img/road1.jpg").convert_alpha(), (0,0))

        # Draw the car in every frame
        car1.run(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()