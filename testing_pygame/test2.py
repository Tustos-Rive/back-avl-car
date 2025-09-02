import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Data Structure Tree")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Example Node class (simplified)
class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), 20)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, BLACK)
        text_rect = text.get_rect(center=(self.x, self.y))
        surface.blit(text, text_rect)

# Create a simple tree
# root = Node(1, screen_width // 2, 50)
# root.left = Node(2, screen_width // 4, 150)
# root.right = Node(3, screen_width * 3 // 4, 150)
# root.left.left = Node(4, screen_width // 8, 250)
# root.left.right = Node(5, screen_width * 3 // 8, 250)

root = Node(1, (screen_width - 50), screen_height // 2)
root.left = Node(5, (root.x - 150), (root.y - 30))
root.right = Node(5, (root.x - 150), (root.y + 30))

# Function to draw connections
def draw_connections(node, surface):
    if node.left:
        pygame.draw.line(surface, BLACK, (node.x, node.y), (node.left.x, node.left.y), 2)
        draw_connections(node.left, surface)
    if node.right:
        pygame.draw.line(surface, BLACK, (node.x, node.y), (node.right.x, node.right.y), 2)
        draw_connections(node.right, surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    draw_connections(root, screen)
    # Draw nodes (order matters for drawing over lines)
    nodes_to_draw = [root]
    while nodes_to_draw:
        current_node = nodes_to_draw.pop(0)
        current_node.draw(screen)
        if current_node.left:
            nodes_to_draw.append(current_node.left)
        if current_node.right:
            nodes_to_draw.append(current_node.right)

    pygame.display.flip()

pygame.quit()