from src.models.obstacle import Obstacle
from src.utils.randoms_utils import RandomsUtils

class Node:
    def __init__(self, value: Obstacle, parent: 'Node' = None):
        # Coordinates (x: int, y: int, type: int)
        self.left: 'Node' = None
        self.right: 'Node' = None
        self.height: int = 1
        self.value = value
        self.parent = parent

    def to_dict(self) -> dict:
        return {
            'value': self.value.to_dict(),
            'left': self.__get_node_dict(), # self.left,
            'right': self.__get_node_dict(True), # self.right,
            'height': self.height
        }

    def __get_node_dict(self, is_right: bool = False, is_parent: bool = False) -> dict | None:
        __return = None
        
        if not is_right and self.left:
                __return = self.left.to_dict()
        elif self.right:
                __return = self.right.to_dict()
        
        return __return
