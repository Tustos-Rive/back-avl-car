from io import TextIOWrapper
import os
import pathlib
from pathlib import Path
import json
from typing import Any

class FilesUtils:
    @staticmethod
    def file_exists(filename: str) -> bool:
        return Path(filename).is_file()
    
    @staticmethod
    def open_file(filename: str, mode: str = 'r') -> TextIOWrapper:
        file = None
        if FilesUtils.file_exists(filename):
            # I Not Use WITH Clausule to NOT close reference automatically
            file = open(filename)
        
        return file
    
    @staticmethod
    def read_file(filename: str) -> Any:
        file = FilesUtils.open_file(filename)
        readed = None

        if file:
            readed = file.read()
            file.close()
        
        return readed
    
    @staticmethod
    def get_filename_from_path(path: str) -> str:
        filename:str = Path(path).name
        return filename

    @staticmethod
    def read_json(filename: str) -> dict:
        data = {}
        readed = FilesUtils.read_file(filename)

        if readed:
            try:
                data['data'] = json.loads(readed)
            except Exception as e:
                # TODO: Add chromologger here
                data['error'] = e
        else:
            data['error'] = f"The file '{FilesUtils.get_filename_from_path(filename)}' don't exists!"

        return data