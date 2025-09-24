from typing import Any

class ResponseSocket:
    def __init__(self, ok: bool, received:Any, msg: str = 'OK', data: Any | None = None, error: Any | None = None):
        self.ok = ok
        self.received = received
        self.msg = msg
        self.data = data
        self.error = error

    def to_dict(self):
        return {
            'ok': self.ok,
            'received': self.received,
            'message': self.msg,
            # TODO: Check that all models are this method -> to_dict()
            'data': self.__get_data(),
            'error': self.error,
        }

    def __get_data(self) -> dict | None:
        if self.data and type(self.data) != str:
            return self.data.to_dict()
        
        return self.data

class BaseFlaskResponse:
    def __init__(self, message: str = '', status: int = 200, ok: bool = True, data: dict = {}, error: Any = None, ) -> None:
        self.status = status
        self.ok = ok
        self.message = message
        self.data = data
        self.error = error

    def to_dict(self) -> dict:
        return {
            'status': self.status,
            'ok': self.ok,
            'message': self.message,
            'data': self.data,
            'error': self.error,
        }

class ReturnModels:
    def __init__(self, message: str = '', ok: bool = True, data: Any = None,error: Any = None):
        self.message = message
        self.ok = ok
        self.data = data
        self.error = error

    def to_dict(self) -> dict:
        return {
            'ok': self.ok,
            'message': self.message,
            'data': self.data,
            'error': self.error,
        }