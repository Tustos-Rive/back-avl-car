from src.controllers.socket_avl_controller import SocketAVLController
from src.models.tree import AVLTree
from src.sockets.socket_manager import SocketManager

class SocketAVLTree:
    def __init__(self, socketIO: SocketManager, tree_model: AVLTree):
        self.socketio = socketIO
        self.tree = tree_model
        self.controller: SocketAVLController = SocketAVLController(tree_model, self.socketio)
        
        # I get a problem, self.socket scure will be None or not ever update... Test...
        self.socketio.namespace = "/AVLTree"
        self.__register_handlers()



    def __register_handlers(self):
        self.socketio.register_handler(False, 'connect', 'connected')
        self.socketio.register_handler(True, 'disconnect', 'disconnected')
        # Insert obstacle, receive (msg, response) because i don't send any *args
        # I Think!
        self.socketio.register_handler(False, "insert_obstacle", "obstacles_inserted", self.controller.emit_obstacle_inserted, True)
        # self.socketio.register_handler(False, "insert_obstacle", "obstacles_inserted", self.tree.setObstacle)
        self.socketio.register_handler(False, "road_inorder", "inorder", self.controller.emit_road_inorder, True)