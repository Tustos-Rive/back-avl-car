from typing import Any

class ResponseSocket:
    def __init__(self, ok: bool, received:Any):
        self.ok = ok
        self.received = received

    def to_dict(self):
        return {
            'ok': self.ok,
            'received': self.received,
        }

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