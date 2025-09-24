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

    # TODO: Seacrh function TYPE, what's the fucking function type? for typing code
    def emit_road_inorder(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        # TODO: Emit/Send the current node to "/AVLTree/inorder" socket every 2 seconds
        # TODO: If not func with time.sleep(2), try learn Threads!!!

        __request_road: ReturnModels = self.avl.inorder()
        __road: list[Obstacle] | None = __request_road.data
        
        if __road:
            print(f'\nRoad :=> {[r.x for r in __road]} ({len(__road)}) \n')
            # In place of a list -> Learn use queue in python (Queue original, real)
            self.__emit_road_inorder(__road, 0, response, emit_name, namespace)

    def emit_obstacle_inserted(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        # TODO: Call the AVLTree controller to try insert obstacle!
        # FIXME: Next, i put just test data, fix this for "real data"!
        response.msg = 'You fuck obstacle has been inserted! madafaka :)'
        emit(emit_name, response.to_dict(), namespace=namespace)

    def __emit_road_inorder(self, road_list: list[Obstacle], index: str, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        if index < len(road_list):
            __obstacle: Obstacle = road_list[index]

            time.sleep(2)
            # TODO: response.data = obstacle_road.id -> Just send the ID of the curent Obstacle
            response.data = __obstacle.id
            # TODO: I need get the EMIT CONTROL, but, i forget that. -> Modify socketManager to can control it!
            print(response.to_dict())

            emit(emit_name, response.to_dict(), namespace=namespace)

            # Call recursively
            self.__emit_road_inorder(road_list, index + 1, response, emit_name, namespace)