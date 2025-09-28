from src.main import Main
from random import randint

from src.models.obstacle import Obstacle
from src.models.tree import AVLTree

if __name__ == '__main__':
    main = Main("*")
    main.socketio.run(main.app, host='localhost', port=4500, debug=True)
    # obstacles = [Obstacle(randint(50, 200), randint(50, 200), randint(1, 11)) for _ in range(10)]
    # obstacles = [Obstacle(13, 5, 3), Obstacle(2, 6, 3),Obstacle(13, 6, 3), Obstacle(4, 5, 3)]

    # tree = AVLTree()

    # for a in obstacles:
    #     inst = tree.insert(a)

    # # tree.to_dict(tree.root)
    # # print(tree.to_dict())
    # tree.print_tree(tree.root)
    # print(tree.search(Obstacle(2, 6, 3)).data.to_dict())

    # tree.delete(Obstacle(2, 6, 3))
    
    # print('\n--------------------------\n')

    # tree.print_tree(tree.root)

    # print(tree.to_dict())


    # print(tree.root.to_dict())

    # ino, pre, pos = [], [], []

    # inorder = tree.inorder().data
    # preorder = tree.preorder().data
    # posorder = tree.posorder().data

    # print("IN", end=': ')
    # for b in inorder:
    #     print(b.to_dict(), end=' ')

    # print("----\n")
    
    # print("PRE", end=': ')
    # for b in preorder:
    #     print(b.to_dict(), end=' ')

    # print("----")

    # print("POS", end=': ')
    # for b in posorder:
    #     print(b.to_dict(), end=' ')

    # print('\n-----\n')

    # tree.print_tree(tree.root)

    # node_value = inorder[randint(0, len(inorder) - 1)]
    # print(f'Node Value: ({node_value.x}, {node_value.y})')
    # # Remove a node!
    # tree.delete(node_value)

    # tree.print_tree(tree.root)

    # Call again to see if error keep!
    # inorder = tree.inorder().data
    # print("IN", end=': ')
    # for b in inorder:
    #     print(b.to_dict(), end=' ')