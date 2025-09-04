import pygame
import sys

pygame.init()

class Configs:
    s_width = 1000
    s_height = 600
    FPS = 60
    
    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (70, 130, 180)
    RED = (220, 20, 60)
    GREEN = (34, 139, 34)
    GRAY = (128, 128, 128)
    
    # Configuración del árbol
    NODE_RADIUS = 25
    FONT_SIZE = 20
    LEVEL_SPACING = 120  # Espaciado horizontal entre niveles
    NODE_SPACING = 80    # Espaciado vertical entre nodos

class AVLNode:
    def __init__(self, value, x=0, y=0):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.height = 1
        
    def draw(self, surface, font):
        # Dibujar círculo del nodo
        pygame.draw.circle(surface, Configs.BLUE, (int(self.x), int(self.y)), Configs.NODE_RADIUS)
        pygame.draw.circle(surface, Configs.BLACK, (int(self.x), int(self.y)), Configs.NODE_RADIUS, 2)
        
        # Dibujar valor del nodo
        text = font.render(str(self.value), True, Configs.WHITE)
        text_rect = text.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(text, text_rect)

class AVLTree:
    def __init__(self):
        self.root = None
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def rotate_right(self, y):
        """Rotación simple a la derecha"""
        x = y.left
        T2 = x.right
        
        # Realizar rotación
        x.right = y
        y.left = T2
        
        # Actualizar alturas
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def rotate_left(self, x):
        """Rotación simple a la izquierda"""
        y = x.right
        T2 = y.left
        
        # Realizar rotación
        y.left = x
        x.right = T2
        
        # Actualizar alturas
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, value):
        """Insertar valor manteniendo propiedades AVL"""
        self.root = self._insert(self.root, value)
        self._calculate_positions()
    
    def _insert(self, node, value):
        # 1. Inserción normal de BST
        if not node:
            return AVLNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            # Valores duplicados no permitidos
            return node
        
        # 2. Actualizar altura del nodo actual
        self.update_height(node)
        
        # 3. Obtener factor de balance
        balance = self.get_balance_factor(node)
        
        # 4. Casos de rotación
        # Caso Left Left
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        
        # Caso Right Right
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        
        # Caso Left Right
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Caso Right Left
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def _calculate_positions(self):
        """Calcular posiciones para visualización horizontal"""
        if not self.root:
            return
        
        # Obtener dimensiones actuales de la ventana
        window_size = pygame.display.get_surface().get_size()
        
        # Posición inicial de la raíz (lado izquierdo)
        start_x = 80
        start_y = window_size[1] // 2
        
        self.root.x = start_x
        self.root.y = start_y
        
        # Calcular posiciones recursivamente
        self._set_positions(self.root, start_x, start_y, 0)
    
    def _set_positions(self, node, x, y, level):
        """Establecer posiciones de forma recursiva - HORIZONTAL"""
        if not node:
            return
        
        node.x = x
        node.y = y
        
        # Para visualización horizontal:
        # - Los niveles avanzan hacia la derecha (incremento en x)
        # - Los hijos se separan verticalmente (diferencia en y)
        
        next_level_x = x + Configs.LEVEL_SPACING
        
        # Calcular el espaciado vertical basado en la altura del subárbol
        vertical_spacing = self._get_subtree_span(node) * Configs.NODE_SPACING / 2
        
        if node.left:
            left_y = y - vertical_spacing / 2
            self._set_positions(node.left, next_level_x, left_y, level + 1)
        
        if node.right:
            right_y = y + vertical_spacing / 2
            self._set_positions(node.right, next_level_x, right_y, level + 1)
    
    def _get_subtree_span(self, node):
        """Calcular el espacio vertical que necesita un subárbol"""
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1
        
        left_span = self._get_subtree_span(node.left) if node.left else 0
        right_span = self._get_subtree_span(node.right) if node.right else 0
        
        return max(1, left_span + right_span)
    
    def draw_connections(self, surface):
        """Dibujar todas las conexiones del árbol"""
        if self.root:
            self._draw_connections_recursive(surface, self.root)
    
    def _draw_connections_recursive(self, surface, node):
        """Dibujar conexiones de forma recursiva"""
        if not node:
            return
        
        # Dibujar conexión al hijo izquierdo
        if node.left:
            pygame.draw.line(
                surface, 
                Configs.BLACK, 
                (int(node.x), int(node.y)), 
                (int(node.left.x), int(node.left.y)), 
                3
            )
            self._draw_connections_recursive(surface, node.left)
        
        # Dibujar conexión al hijo derecho
        if node.right:
            pygame.draw.line(
                surface, 
                Configs.BLACK, 
                (int(node.x), int(node.y)), 
                (int(node.right.x), int(node.right.y)), 
                3
            )
            self._draw_connections_recursive(surface, node.right)
    
    def draw_all_nodes(self, surface, font):
        """Dibujar todos los nodos usando BFS"""
        if not self.root:
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            current.draw(surface, font)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    def get_tree_info(self):
        """Obtener información del árbol para debugging"""
        if not self.root:
            return "Árbol vacío"
        
        height = self.get_height(self.root)
        node_count = self._count_nodes(self.root)
        
        return f"Altura: {height}, Nodos: {node_count}"
    
    def _count_nodes(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

def main():
    # Inicializar pygame
    screen = pygame.display.set_mode((Configs.s_width, Configs.s_height), pygame.RESIZABLE)
    pygame.display.set_caption("Árbol AVL Horizontal - Santiago")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, Configs.FONT_SIZE)
    info_font = pygame.font.Font(None, 24)
    
    # Crear árbol AVL
    avl_tree = AVLTree()
    
    # Valores de ejemplo para probar
    test_values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35]
    
    running = True
    show_instructions = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.VIDEORESIZE:
                # Recalcular posiciones al redimensionar
                avl_tree._calculate_positions()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Insertar valores de ejemplo
                    for value in test_values:
                        avl_tree.insert(value)
                
                elif event.key == pygame.K_c:
                    # Limpiar árbol
                    avl_tree.root = None
                
                elif event.key == pygame.K_r:
                    # Insertar valor aleatorio
                    import random
                    avl_tree.insert(random.randint(1, 100))
                
                elif event.key == pygame.K_h:
                    # Toggle de instrucciones
                    show_instructions = not show_instructions
        
        # Limpiar pantalla
        screen.fill(Configs.WHITE)
        
        # Dibujar árbol
        avl_tree.draw_connections(screen)
        avl_tree.draw_all_nodes(screen, font)
        
        # Mostrar información
        info_text = info_font.render(avl_tree.get_tree_info(), True, Configs.BLACK)
        screen.blit(info_text, (10, 10))
        
        # Mostrar instrucciones
        if show_instructions:
            instructions = [
                "ESPACIO: Insertar valores de ejemplo",
                "R: Insertar valor aleatorio",
                "C: Limpiar árbol",
                "H: Ocultar/mostrar ayuda"
            ]
            
            for i, instruction in enumerate(instructions):
                text = info_font.render(instruction, True, Configs.BLACK)
                screen.blit(text, (10, 50 + i * 25))
        
        pygame.display.flip()
        clock.tick(Configs.FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()