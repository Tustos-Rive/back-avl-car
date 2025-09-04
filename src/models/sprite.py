import pygame

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