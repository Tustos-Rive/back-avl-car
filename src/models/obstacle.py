# Should have a RECT collider for collide with the CAR
# Every Node have a collider

from src.utils.randoms_utils import RandomsUtils


class Obstacle:
    def __init__(self, x: float, y: float, type_id: int) -> None:
        self.id = RandomsUtils.random_id(8, 2)
        self.x = x
        self.y = y
        self.type_id = type_id

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'type_id': self.type_id,
        }