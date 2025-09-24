from typing import Any
from flask import Flask
from src.models.responses import BaseFlaskResponse
from src.routers.Router import Router

class MainRoute(Router):
    def __init__(self, app: Flask, jsonify: Any) -> None:
        super().__init__(app, jsonify)

        self.__register_routes()

    def __register_routes(self):
        self.register_routes("/", self.__home)

    def __home(self):
        response = BaseFlaskResponse('Hello From Flask!')
        return self.jsonify(response.to_dict())