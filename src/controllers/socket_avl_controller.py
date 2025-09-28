import time
from typing import Any

from flask_socketio import emit
from src.models.obstacle import Obstacle
from src.models.responses import ResponseSocket, ReturnModels
from src.models.tree import AVLTree
from src.sockets.socket_manager import SocketManager

class SocketAVLController:
    def __init__(self, tree_model: AVLTree, socketio: SocketManager) -> None:
        self.avl = tree_model
        self.socketio = socketio

    def get_tree_avl(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        # TODO: I don't think all, but, by now, just this
        response.msg = 'This is the tree by moment!'

        # send the AVLTree in current state or NONE, anyway 
        response.data = self.avl
        print(f"\nGet Tree Response <=> {response.to_dict()}\n")
        emit(emit_name, response.to_dict(), namespace=namespace)

    # TODO: Seacrh function TYPE, what's the fucking function type? for typing code
    def emit_road(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str, road_name: str) -> None:
        __request_road: ReturnModels | None = None

        # Call case road name
        match road_name:
            case 'preorder':
                __request_road = self.avl.preorder()
            case 'inorder':
                __request_road = self.avl.inorder()
            case 'posorder':
                __request_road = self.avl.posorder()
            case _:
                print('Please send me the Road Name (inorder, posorder or preorder)')
                return

        __road: list[Obstacle] | None = __request_road.data
        
        if __road:
            print(f'\nRoad {road_name} :=> {[r.x for r in __road]} ({len(__road)}) \n')

            self.__emit_road(__road, 0, response, emit_name, namespace)

    def emit_avl_reseted(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        # PYTHON IS A fucking SHIT!
        # In other i can re-write with the same type!!!!
        # self.avl = AVLTree()

        self.avl.reset()
        
        response.data = self.avl

        print(f'\n{self.avl.print_tree(self.avl.root)}\n')

        emit(emit_name, response.to_dict(), namespace=namespace)

    def emit_obstacle_removed(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        # TODO: Test this, send from client a event remove
        try:
            self.avl.delete(msg)
            response.msg = 'You fuck obstacle has been removed! madafaka :)'
            response.data = self.avl
        except Exception as e:
            response.msg = 'Not was possible remode the obstacle'
            response.error = e.__str__()
        
        emit(emit_name, response.to_dict(), namespace=namespace)

    def __emit_road(self, road_list: list[Obstacle], index: str, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        if index < len(road_list):
            __obstacle: Obstacle = road_list[index]

            time.sleep(1)
            response.data = __obstacle.id

            # TODO: Remove me!
            print(f'\nResponse to send: {response.to_dict()}\n')

            emit(emit_name, response.to_dict(), namespace=namespace)

            # Call recursively
            self.__emit_road(road_list, index + 1, response, emit_name, namespace)