from flask import Flask, jsonify
from flask_cors import CORS
from src.models.car import Car
from src.models.node import Node
from src.models.road import Road
from src.models.tree import AVLTree
from src.routers.main_route import MainRoute
from src.sockets.socket_avl_tree import SocketAVLTree
from src.sockets.socket_manager import SocketManager

class Main:
    def __init__(self, origins_allowed: str, supports_credentials: bool = True):
        # Flask app main
        self.app = Flask(__name__)
        # From where accept connections
        self.origins = origins_allowed
        self.supports_credentials = supports_credentials

        # Models instances
        self.AVLTree = AVLTree()
        self.Road = Road()
        self.Node = Node()
        self.Car = Car()

        # Socket Main Manager
        self.socketio = None

        # Call configs
        self.__configs()
    
    def __configs(self):
        # Allow requests only from...
        CORS(self.app, origins=self.origins, supports_credentials=self.supports_credentials)
        self.socketio = SocketManager(self.app, self.origins) # SocketIO(app, "*")
        
        # Call routes
        MainRoute(self.app, jsonify)
        
        # Call sockets managers
        SocketAVLTree(self.socketio, self.AVLTree)

    def run_main(self) -> None:
        # SocketAVLTree(self.app, self.origins, self.AVLTree)
        # SocketAVLTree(self.socketio, self.app, self.origins, self.AVLTree)
        pass