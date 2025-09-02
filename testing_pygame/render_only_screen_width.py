import pygame
import random as rd
pygame.init()

class Configs:
    s_width = 400
    s_height = 350

screen = pygame.display.set_mode((Configs.s_width, Configs.s_height), flags=pygame.RESIZABLE)
pygame.display.set_caption("Render Only Screen Width - Visible")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Node Class
class Node:
    def __init__(self, value, x=0, y=0):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.parent = None

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), 20)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, BLACK)
        text_rect = text.get_rect(center=(self.x, self.y))
        surface.blit(text, text_rect)

class BTS:
    def __init__(self):
        self.root = None

    # Insert a new value into the BST
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            window_size = pygame.display.get_window_size()
            new_node.x = (window_size[0] - 50)
            new_node.y = window_size[1] // 2
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node:Node, new_node:Node):
        new_node.x = current_node.x - 50
        
        if self.search(new_node.value):
            return
        if new_node.value < current_node.value:
            # print(f"I'm in left side: NewNode({new_node.value}) || CurrentNode({current_node.value})")
            # Set the left coordinates
            new_node.y = current_node.y - 30

            if current_node.left is None:
                current_node.left = new_node
                new_node.parent = current_node
            else:
                self._insert(current_node.left, new_node)
        else:
            # print(f"I'm in right side: NewNode({new_node.value}) || CurrentNode({current_node.value})")
            new_node.y = current_node.y + 30

            if current_node.right is None:
                current_node.right = new_node
                new_node.parent = current_node
            else:
                self._insert(current_node.right, new_node)

    # Search for a value in the BST
    def search(self, value):
        if(self.root is None):
            # print("The tree is empty.")
            return None
        else:
            return self._search(self.root, value)

    def _search(self, current_node:Node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search(current_node.left, value)
        return self._search(current_node.right, value)

    # Test method insert, not tree AVL, just BTS
    # def _insert(self, current_node:Node, new_node:Node):
    #     new_node.x = current_node.x - 50
    #     if self.search(new_node.value):
    #         # print("The node already exists!")
    #         return
    #     elif new_node.value < current_node.value:
    #         # print(f"I'm in left side: NewNode({new_node.value}) || CurrentNode({current_node.value})")
    #         # Set the left coordinates
    #         new_node.y = current_node.y - 30

    #         if not current_node.left:
    #             current_node.left = new_node
    #         else:
    #             self._insert(current_node.left, new_node)
    #     else:
    #         # print(f"I'm in right side: NewNode({new_node.value}) || CurrentNode({current_node.value})")
    #         new_node.y = current_node.y + 30
    #         if not current_node.right:
    #             current_node.right = new_node
    #         else:
    #             self._insert(current_node.right, new_node)

    def recalculate_nodes_axis(self):
        window_size = pygame.display.get_window_size()
        self.root.x = (window_size[0] - 50)
        self.root.y = window_size[1] // 2

        self._recalculate_nodes_axis(self.root)
    
    def _recalculate_nodes_axis(self, current_node):
        if current_node:            
            current_node.x = current_node.parent.x - 50

            current_node.y = current_node.parent.y - 30
            self._recalculate_nodes_axis(current_node.left)

            current_node.y = current_node.parent.y + 30
            self._recalculate_nodes_axis(current_node.right)


# DrawConnections Method
def draw_connections(node, surface):
    if node.left:
        pygame.draw.line(surface, BLACK, (node.x, node.y), (node.left.x, node.left.y), 2)
        draw_connections(node.left, surface)
    if node.right:
        pygame.draw.line(surface, BLACK, (node.x, node.y), (node.right.x, node.right.y), 2)
        draw_connections(node.right, surface)

# ViewPort
# Some more easy, is validate if the obstacle.x and obstacle.y are in the screen range
# if (obctacle.x > 0 and obstacle.x < s_width) and obctacle.y > 0 and obstacle.y < s_height
# camera_rect = pygame.Rect(0, Configs.s_height, Configs.s_width, Configs.s_height)

# root = Node(1, (Configs.s_width - 50), Configs.s_height // 2)
# root.left = Node(5, (root.x - 50), (root.y - 30))
# root.right = Node(5, (root.x - 50), (root.y + 30))

###################
# Tree Tests
tree_obstacles = BTS()

obstacles_values_node = []
flag = True
while flag:
    value_random = rd.randint(0, 300)
    if not value_random in obstacles_values_node:
        obstacles_values_node.append(value_random)

    if len(obstacles_values_node) == 100:
        flag = False


for value in obstacles_values_node:
    tree_obstacles.insert(value)

#############

# MainLoop Flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Resize Screen
        if event.type == pygame.VIDEORESIZE:
            # To can er-calculate the axis in x
            tree_obstacles.root = None
            new_w, new_h = pygame.display.get_window_size()

            screen = pygame.display.set_mode((new_w, new_h), flags=pygame.RESIZABLE)
            # Add again the nodes to the tree (For re-calculate the coordenates, i think that)
            for value in obstacles_values_node:
                tree_obstacles.insert(value)

            # tree_obstacles.recalculate_nodes_axis()

    screen.fill((255, 255, 255))
    draw_connections(tree_obstacles.root, screen)

    # nodes_to_draw = [root]
    nodes_to_draw = [tree_obstacles.root]
    while nodes_to_draw:
        current_node = nodes_to_draw.pop(0)
        current_node.draw(screen)
        if current_node.left:
            nodes_to_draw.append(current_node.left)
        if current_node.right:
            nodes_to_draw.append(current_node.right)
    
    pygame.display.flip()

pygame.quit()