from typing import Any
from flask import Flask, Response
from src.controllers.data_controller import DataController
from src.models.responses import BaseFlaskResponse
from src.routers.Router import Router

class DataRouter(Router):
    def __init__(self, app: Flask, jsonify: Any, data_folder: str) -> None:
        super().__init__(app, jsonify)
        self.controller = DataController(self.jsonify, data_folder)

        self.__register_routes()

    def __register_routes(self) -> None:
        self.register_routes("/data", self.__home_data)
        self.register_routes("/data/json/<filename>", self.__get_file_json)

    def __home_data(self) -> Response:
        return self.controller.get_home()
    
    def __get_file_json(self, filename: str) -> Response:
        return self.controller.get_json(filename)