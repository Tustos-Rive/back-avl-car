class Node:
    def __init__(self, value: str, parent: 'Node' | None = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def to_dict(self) -> dict:
        return {
            'value': self.value,
            'left': self.left,
            'right': self.right,
            # Parent.dict or None (ROOT.parent == None)
            'parent': self.parent.to_dict() if self.parent else self.parent,
        }