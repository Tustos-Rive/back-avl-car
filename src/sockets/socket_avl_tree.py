from src.models.tree import AVLTree
from src.sockets.socket_manager import SocketManager

class SocketAVLTree:
    def __init__(self, socketIO: SocketManager, tree_model: AVLTree):
        # super().__init__(app, cors, "/AVLTree")
        self.socketio = socketIO
        self.tree = tree_model

        self.socketio.namespace = "/AVLTree"
        self.__register_handlers()

    def __register_handlers(self):
        self.socketio.register_handler(False, 'connect', 'connected')
        self.socketio.register_handler(True, 'disconnect', 'disconnected')
        # Insert obstacle, receive (msg, response) because i don't send any *args
        # I Think!
        self.socketio.register_handler(False, "insert_obstacle", "obstacles_inserted", self.tree.setObstacle)