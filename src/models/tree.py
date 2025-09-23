from src.models.node import Node
from src.models.obstacle import Obstacle
from src.models.responses import ReturnModels

# def setObstacle(data: dict, *args) -> None:
#     print(f'Obstacle added: {data}, and get this args: ', *args)

class AVLTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    # Insert a new value into the BST
    def insert(self, value: Obstacle) -> ReturnModels:
        node: ReturnModels = self.search(value)
        response: ReturnModels = ReturnModels(f'The node with coordinates ({value.x}, {value.y}) has been added successfully!')

        # not None = node...
        if(node.data):
            response.ok = False
            response.message = f'Node with coordinates ({value.x}, {value.y}) already exists.'
        else:
            new_node: Node = Node(value)
            # (not some) == (some is None) == (!some) == (~some)
            if not self.root:
                self.root = new_node
            else:
                self.root = self._insert(self.root, new_node)
        return response

    def _insert(self, current_node: Node, new_node: Node) -> Node:
        if current_node:
            if new_node.value.x < current_node.value.x:
                if not current_node.left:
                    current_node.left = new_node
                    new_node.parent = current_node
                else:
                    # In this case current.left is none, so, not in on this, and execute _rebalance()
                    current_node.left = self._insert(current_node.left, new_node)
            else:
                if not current_node.right:
                    current_node.right = new_node
                    new_node.parent = current_node
                else:
                    current_node.right = self._insert(current_node.right, new_node)

        # AUpdate the currentNode height
        self.update_height(current_node)
        
        # Balance the currentNode and return if have any rotation
        return self._rebalance(current_node)

    # Search for a value in the BST
    def search(self, value: Obstacle) -> ReturnModels:
        response: ReturnModels = ReturnModels()

        if(not self.root):
            response.message = 'The tree is empty!'
            response.ok = False
        else:
            node: Node = self._search(self.root, value)
            
            # Case node found!
            if node:
                response.message = 'Node found, see data!'
                response.data = node
            else:
                response.ok = False
                response.message = "Node DON'T found!"

        return response

    def _search(self, current_node: Node, value: Obstacle) -> Node | None:
        if not current_node or (current_node.value.x == value.x and current_node.value.y == value.y):
            return current_node
        if value.x < current_node.value.x:
            return self._search(current_node.left, value)
        return self._search(current_node.right, value)

    # Find the inorder predecessor (the maximum in the left subtree)
    def _getPredecessor(self, node: Node) -> Node | None:
        if node.left:
            current: Node = node.left
            while current.right:
                current = current.right
            return current
        return None

    # Replace one subtree with another (adjusts parent references)
    def changeNodePosition(self, node_to_replace: Node, new_subtree_root: Node):
        if not node_to_replace.parent:  # If replacing the root
            self.root = new_subtree_root
        else:
            if node_to_replace == node_to_replace.parent.left:
                node_to_replace.parent.left = new_subtree_root
            else:
                node_to_replace.parent.right = new_subtree_root
        if new_subtree_root:
            new_subtree_root.parent = node_to_replace.parent

    # Delete a node by value
    def delete(self, value: Obstacle):
        node_to_delete = self.search(value).data
        if node_to_delete:
            self._delete(node_to_delete)

    def _delete(self, node_to_delete: Node):
        # Case 1: node is a leaf (no children)
        if not node_to_delete.left and not node_to_delete.right:
            self.changeNodePosition(node_to_delete, None)
            return

        # Case 2: node has two children
        if node_to_delete.left and node_to_delete.right:
            predecessor: Node = self._getPredecessor(node_to_delete)
            if predecessor.parent != node_to_delete:  # predecessor is not a direct child
                self.changeNodePosition(predecessor, predecessor.left)
                predecessor.left = node_to_delete.left
                predecessor.left.parent = predecessor
            self.changeNodePosition(node_to_delete, predecessor)
            predecessor.right = node_to_delete.right
            predecessor.right.parent = predecessor
            return

        # Case 3: node has only one child
        if node_to_delete.left:
            self.changeNodePosition(node_to_delete, node_to_delete.left)
        else:
            self.changeNodePosition(node_to_delete, node_to_delete.right)

    # Inorder traversal (left → root → right)
    def inorder(self):
        response = ReturnModels()
        if not self.root:
            response.message = "Don't was possible get road"
            response.error = 'Tree is empty!'
        else:
            response.data = self.__inorder(self.root)
        
        return response

    def __inorder(self, current_node: Node, road: list[int] = []):
        # when current is a leaft, when call again, LEAFT Not have childs...
        if current_node:
            if current_node.left:
                self.__inorder(current_node.left, road)

            # Add the node value to the road
            # road.append(current_node.value.to_dict())
            road.append(current_node.value)

            if current_node.right:
                self.__inorder(current_node.right, road)

            return road
    
    # Posorder (left →  right → root)
    def posorder(self):
        response = ReturnModels()
        if not self.root:
            response.message = "Don't was possible get road"
            response.error = 'Tree is empty!'
        else:
            response.data = self.__posorder(self.root)
        
        return response

    def __posorder(self, current_node: Node, road: list[int] = []):
        # when current is a leaft, when call again, LEAFT Not have childs...
        if current_node:
            if current_node.left:
                self.__posorder(current_node.left, road)

            if current_node.right:
                self.__posorder(current_node.right, road)

            # Add the node value to the road
            # road.append(current_node.value.to_dict())
            road.append(current_node.value)
            
            return road
    
    # Preorder (root → left → right)
    def preorder(self):
        response = ReturnModels()
        if not self.root:
            response.message = "Don't was possible get road"
            response.error = 'Tree is empty!'
        else:
            response.data = self.__preorder(self.root)
        
        return response

    def __preorder(self, current_node: Node, road: list[int] = []):
        # when current is a leaft, when call again, LEAFT Not have childs...
        if current_node:
            # Add the node value to the road
            # road.append(current_node.value.to_dict())
            road.append(current_node.value)

            if current_node.left:
                self.__preorder(current_node.left, road)

            if current_node.right:
                self.__preorder(current_node.right, road)

            return road

    def get_height(self, node: Node):
        return node.height if node else 0

    def update_height(self, node: Node):
        # Set the max beetwen the left side and the right side!
        # Is 1+max(left, right), because is UPDATE, means that I add new node
        # Ever height is UP (+)
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance_factor(self, node: Node):
        # BALANCE FACTOR = BF
        # BF = (HEIGHT-LEFT-SIDE) - (HEIGHT-RIGHT-SIDE)
        # BF == OK, when BF is in range [-1, 0, 1] 
        # Other out range is BAD
        # If don't exists node BF = 0
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def _rebalance(self, node: Node) -> Node:
        """Balance the AVL tree"""
        if not node:
            return node

        balance_factor = self.get_balance_factor(node)
        
        # Left Heavy (L)
        if balance_factor > 1:
            # Case LR (Left-Right)
            if self.get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            
            # Just the L rotation
            return self._rotate_right(node)
        
        # Right Heavy (R)  
        if balance_factor < -1:
            # Case RL (Right-Left)
            if self.get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            
            # Just the R rotation
            return self._rotate_left(node)
        
        return node

    def _rotate_right(self, old_root: Node) -> Node:
        """Right totation and update parents"""
        new_root: Node = old_root.left
        subtree: Node = new_root.right

        # Rotate
        new_root.right = old_root
        old_root.left = subtree

        # Update parents
        new_root.parent = old_root.parent
        old_root.parent = new_root
        if subtree:
            subtree.parent = old_root

        # Update nodes height
        self.update_height(old_root)
        self.update_height(new_root)

        return new_root

    def _rotate_left(self, old_root: Node) -> Node:
        """Left Rotation"""
        new_root: Node = old_root.right
        subtree: Node = new_root.left

        # Rotate
        new_root.left = old_root
        old_root.right = subtree

        # Update parents
        new_root.parent = old_root.parent
        old_root.parent = new_root
        if subtree:
            subtree.parent = old_root

        # Update heights
        self.update_height(old_root)
        self.update_height(new_root)

        return new_root

    # Method to print the tree in console
    def print_tree(self, node: Node | None = None, prefix: str = "", is_left: bool = True):
        if node:
            # Print right subtree
            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                self.print_tree(node.right, new_prefix, False)

            # Print current node
            connector = "└── " if is_left else "┌── "
            print(prefix + connector + str((node.value.x, node.value.y)))

            # Print left subtree
            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                self.print_tree(node.left, new_prefix, True)