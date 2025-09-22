from typing import Any
from flask import Response
from src.models.responses import BaseFlaskResponse

class AVLController:
    def __init__(self, jsonify: Any):
        self.jsonify = jsonify
    
    def get_home(self) -> Response:
        response = BaseFlaskResponse('Welcome to AVL section!')
        return self.jsonify(response.to_dict())
    
    def add_node(self):
        pass