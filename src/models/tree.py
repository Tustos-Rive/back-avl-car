from src.models.node import Node
from src.models.responses import ReturnModels

# def setObstacle(data: dict, *args) -> None:
#     print(f'Obstacle added: {data}, and get this args: ', *args)

class AVLTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    # Insert a new value into the BST
    def insert(self, value: str) -> ReturnModels:
        node: ReturnModels = self.search(value)
        response: ReturnModels = ReturnModels()

        # not None = node...
        if(node):
            # TODO: Changes value(str) to value(dict{x: int, y: int, type: int})
            response.message = f'Node with coordinates ({value}) already exists.'
        else:
            new_node: Node = Node(value)
            # (not some) == (some is None) == (!some) == (~some)
            if not self.root:
                self.root = new_node
            else:
                self._insert(self.root, new_node)
                response.message = f'The node with coordinates ({value}) has been added successfully!'
        return response

    def _insert(self, current_node, new_node):
        # TODO: Make a copy of this colab code in my github! and put link here
        # What if node not exists?, check the original: https://colab.research.google.com/drive/11xYZ6pbe0sd9aYdjLoAyJvjPS5BVOUZ6#scrollTo=dOci0KVNuRXV
        if current_node:
            # new_node.x is less that current.x
            # TODO: Change just "value" for "value.x" or similar
            if new_node.value < current_node.value:
                # Don't exists a left child in current
                if not current_node.left:
                    current_node.left = new_node
                    new_node.parent = current_node
                else:
                    # Call recursive by left side
                    self._insert(current_node.left, new_node)
            # new_node.x is greather that current.x 
            else:
                # Don't exists a right child in current
                if not current_node.right:
                    current_node.right = new_node
                    new_node.parent = current_node
                else:
                    # Call recursive by right side
                    self._insert(current_node.right, new_node)

    # Search for a value in the BST
    # TODO: Change value sintx from str/int to dict{x: int, y: int, type: int}
    def search(self, value) -> ReturnModels:
        response: ReturnModels = ReturnModels()

        if(self.root):
            response.message = 'The tree is empty!'
        else:
            # Case node found!
            node: Node = self._search(self.root, value)
            response.message = 'Node found, see data!'
            response.data = node.to_dict()

        return response

    def _search(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search(current_node.left, value)
        return self._search(current_node.right, value)

    # Find the inorder predecessor (the maximum in the left subtree)
    def _getPredecessor(self, node):
        if node.left is not None:
            current = node.left
            while current.right is not None:
                current = current.right
            return current
        return None

    # Replace one subtree with another (adjusts parent references)
    def changeNodePosition(self, node_to_replace, new_subtree_root):
        if node_to_replace.parent is None:  # If replacing the root
            self.root = new_subtree_root
        else:
            if node_to_replace == node_to_replace.parent.left:
                node_to_replace.parent.left = new_subtree_root
            else:
                node_to_replace.parent.right = new_subtree_root
        if new_subtree_root is not None:
            new_subtree_root.parent = node_to_replace.parent

    # Delete a node by value
    def delete(self, value):
        node_to_delete = self.search(value)
        if node_to_delete is not None:
            self._delete(node_to_delete)

    def _delete(self, node_to_delete):
        # Case 1: node is a leaf (no children)
        if node_to_delete.left is None and node_to_delete.right is None:
            self.changeNodePosition(node_to_delete, None)
            return

        # Case 2: node has two children
        if node_to_delete.left is not None and node_to_delete.right is not None:
            predecessor = self._getPredecessor(node_to_delete)
            if predecessor.parent != node_to_delete:  # predecessor is not a direct child
                self.changeNodePosition(predecessor, predecessor.left)
                predecessor.left = node_to_delete.left
                predecessor.left.parent = predecessor
            self.changeNodePosition(node_to_delete, predecessor)
            predecessor.right = node_to_delete.right
            predecessor.right.parent = predecessor
            return

        # Case 3: node has only one child
        if node_to_delete.left is not None:
            self.changeNodePosition(node_to_delete, node_to_delete.left)
        else:
            self.changeNodePosition(node_to_delete, node_to_delete.right)

    # Inorder traversal (left → root → right)
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node.value, end=" ")
        if node.right:
            self.inorder(node.right)

    # Method to print the tree in console
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is not None:
            # Print right subtree
            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                self.print_tree(node.right, new_prefix, False)

            # Print current node
            connector = "└── " if is_left else "┌── "
            print(prefix + connector + str(node.value))

            # Print left subtree
            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                self.print_tree(node.left, new_prefix, True)