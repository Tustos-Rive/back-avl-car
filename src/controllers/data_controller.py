from typing import Any
from flask import Response
from src.models.responses import BaseFlaskResponse
from src.utils.files_utils import FilesUtils
from src.utils.others_utils import Utils


class DataController:
    def __init__(self, jsonify: Any, data_folder: str):
        self.jsonify = jsonify
        self.data_folder = data_folder

    def get_home(self) -> Response:
        reponse = BaseFlaskResponse('Welcome to Data section!')
        return self.jsonify(reponse.to_dict())

    def get_json(self, filename: str) -> Response:
        # folder/filename.extension
        __filename = f'{self.data_folder}{filename}'
        response = BaseFlaskResponse(f"You're trying get the file: '{filename}'")

        # Try read JSON (If exists)
        content: dict = FilesUtils.read_json(__filename)

        if content.get('error'):
            # Data bring a error, send these ERROR
            response.error = content.get('error')
            response.ok = False
            # Bad Request!
            response.status = 400
        else:
            # Not have errors, just add the get data
            response.data = content.get('data')
            response.message = f"'data' is the conent of '{filename}' file!"

        return self.jsonify(response.to_dict())