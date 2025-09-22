from typing import Any
from flask import Flask, Response
from src.controllers.avl_controller import AVLController
from src.models.responses import BaseFlaskResponse
from src.routers.Router import Router

class AVLRouter(Router):
    def __init__(self, app: Flask, jsonify: Any) -> None:
        super().__init__(app, jsonify)
        self.controller: AVLController = AVLController(jsonify)
        
        self.__register_routes()

    def __register_routes(self) -> None:
        self.register_routes("/avl", self.__home_avl)

    def __home_avl(self) -> Response:
        return self.controller.get_home()