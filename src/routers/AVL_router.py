from typing import Any
from flask import Flask, Response, request
from src.controllers.avl_controller import AVLController
from src.models.responses import BaseFlaskResponse
from src.models.tree import AVLTree
from src.routers.Router import Router

class AVLRouter(Router):
    def __init__(self, app: Flask, jsonify: Any, tree_model: AVLTree) -> None:
        super().__init__(app, jsonify)
        self.endpoint = '/avl'
        self.controller: AVLController = AVLController(jsonify, tree_model)
        
        self.__register_routes()

    def __register_routes(self) -> None:
        self.register_routes(f"{self.endpoint}", self.__home_avl)
        self.register_routes(f"{self.endpoint}/node/add", self.__node_add, 'POST', 'GET', 'OPTIONS', 'HEAD')

    def __home_avl(self) -> Response:
        return self.controller.get_home()
    
    def __node_add(self) -> Response:
        body = request.json
        return self.controller.add_node(body)