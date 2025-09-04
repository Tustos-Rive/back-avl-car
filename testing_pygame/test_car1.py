import pygame

# from src.models.car import Car
# from src.models.sprite import MySprite

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()  # Call the parent class (Sprite) constructor

        # Load the sprite image
        self.image = pygame.image.load(image_path).convert_alpha()
        # .convert_alpha() handles transparency

        # Create a Rect object from the image's dimensions
        self.rect = self.image.get_rect()

        # Set the initial position of the sprite
        self.rect.topleft = (x, y)

class Car:
    def __init__(self, sprite:MySprite, battery:int, window_size:tuple[int], velocity:float = 5):
        # sprite -> img
        # Velocity -> float
        # battery -> int|float
        # collition_with_obstacle -> bool
        self.sprite = sprite
        self.velocity = velocity
        self.battery = battery
        self.collition_with_obstacle = False
        self.pos_x = 100
        self.pos_y = window_size[1] // 2

    def run(self, screen:pygame.Surface):
        if self.pos_x < screen.get_size()[0] - 200:
            self.pos_x += self.velocity
        else:
            self.pos_x = 50
        self.draw(screen)

    def draw(self, screen:pygame.Surface):
        self.sprite.rect.x = self.pos_x
        screen.blit(self.sprite.image, self.sprite.rect)

def main():
    pygame.init()

    FPS = 60
    screen = pygame.display.set_mode((800, 500))
    pos_x, pos_y = pygame.display.get_window_size()
    car_sprite = MySprite("car1.png", 50, pos_y - 200)

    car1 = Car(car_sprite, 100, (pos_x, pos_y))

    clock = pygame.time.Clock()

    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        screen.fill((55, 255, 0))

        car1.run(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()