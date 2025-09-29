from src.main import Main
from random import randint

from src.models.obstacle import Obstacle
from src.models.tree import AVLTree
from src.utils.others_utils import Utils

if __name__ == '__main__':
    main = Main("*")
    main.socketio.run(main.app, host='localhost', port=4500, debug=True)