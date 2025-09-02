import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

def draw_tree(node, x, y, dx):
    if node is None:
        return
    # Dibujar el nodo
    pygame.draw.circle(screen, (0, 128, 0), (x, y), 20)
    font = pygame.font.SysFont(None, 24)
    img = font.render(str(node['value']), True, (255, 255, 255))
    screen.blit(img, (x - 10, y - 10))
    
    # Dibujar hijos
    if 'left' in node and node['left'] is not None:
        pygame.draw.line(screen, (0,0,0), (x, y), (x - dx, y + 60), 2)
        draw_tree(node['left'], x - dx, y + 60, dx // 2)
    if 'right' in node and node['right'] is not None:
        pygame.draw.line(screen, (0,0,0), (x, y), (x + dx, y + 60), 2)
        draw_tree(node['right'], x + dx, y + 60, dx // 2)

tree = {
    'value': 1,
    'left': {'value': 2, 'left': None, 'right': None},
    'right': {'value': 3, 'left': None, 'right': None}
}

draw_tree(tree, 400, 50, 100)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
