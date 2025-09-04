# Should check/validate if collide with the Obstacle object|Node
from pygame import Surface, display
from .sprite import MySprite

class Car:
    def __init__(self, sprite:MySprite, battery:int, window_size:tuple[int, int], velocity:float = 5):
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

    def run(self, screen:Surface):
        # Todo: SOLID
        if self.pos_x < screen.get_size()[0] - 200:
            self.pos_x += self.velocity
        else:
            self.pos_x = 50
        self.draw(screen)

    def draw(self, screen:Surface):
        """Draw indefinitely the car, and move...
        
        Args:
            `screen:Surface`: _description_
        """
        # Todo: SOLID
        self.sprite.rect.x = self.pos_x
        self.sprite.rect.y = self.pos_y
        screen.blit(self.sprite.image, self.sprite.rect)

    def up(self):
        # Just Testing
        print(f'Up | X: {self.pos_x} | y: {self.pos_y} |')
        # Todo: Better this
        if self.pos_y > 50:
            self.pos_y -= 50

    def down(self):
        # Just Testing
        print(f'Down | X: {self.pos_x} | y: {self.pos_y} |')
        # Todo: Better this
        if self.pos_y < display.get_window_size()[1] - 150:
            self.pos_y += 50