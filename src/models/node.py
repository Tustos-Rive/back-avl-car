from src.models.obstacle import Obstacle
from src.utils.randoms_utils import RandomsUtils

class Node:
    def __init__(self, value: Obstacle, parent: 'Node' = None):
        # Coordinates (x: int, y: int, type: int)
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1

    def to_dict(self) -> dict:
        return {
            'value': self.value.to_dict(),
            'left': self.left,
            'right': self.right,
            'height': self.height,
            # Parent.dict or None (ROOT.parent == None)
            'parent': self.parent.to_dict() if self.parent else self.parent,
        }