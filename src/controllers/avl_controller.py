from typing import Any
from flask import Response
from src.models.obstacle import Obstacle
from src.models.responses import BaseFlaskResponse
from src.models.tree import AVLTree

class AVLController:
    def __init__(self, jsonify: Any, tree_model: AVLTree):
        self.jsonify = jsonify
        self.avl = tree_model
    
    def get_home(self) -> Response:
        response = BaseFlaskResponse('Welcome to AVL section!')
        return self.jsonify(response.to_dict())
    
    def add_node(self, data) -> Response:
        response = BaseFlaskResponse()

        try:
            print(data)
            # for obstacle in data:
            #     print(obstacle)
            __obstacle = Obstacle(data.get('x'), data.get('y'), data.get('type_id'))
            __insert = self.avl.insert(__obstacle)

            response.message = __insert.message
            
            if not __insert.ok:
                response.status = 400
            
            response.ok = __insert.ok
            response.data = __insert.data
        except Exception as e:
            print('Exception Catched: ', e)
            response.error = 'Has been ocurred something when try add node!'
            response.status = 500
            response.error = e.__str__()

        print(f'Data to send, add_node => {response.to_dict()}')
        
        self.avl.print_tree(self.avl.root)
        return self.jsonify(response.to_dict())