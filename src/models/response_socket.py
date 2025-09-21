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