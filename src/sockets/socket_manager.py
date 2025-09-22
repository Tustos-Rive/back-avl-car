from typing import Any
from flask import Flask
from flask_socketio import SocketIO, emit
from src.models.response_socket import ResponseSocket

class SocketManager(SocketIO):
    # def __init__(self, socketio: SocketIO, app: Flask):
    def __init__(self, app: Flask, cors: str, namespace: str = "/") -> None:
        super().__init__(app, cors_allowed_origins=cors)

        # Channel
        self.namespace = namespace

        # Register the basics handlers (Connect & Disconnect)
        self.__register_basics_handlers()

    def register_handler(self, not_channel = True, event_name: str = '', emit_name: str = '', callback = None, *callback_args):
        # Call the handle_event()
        # When are the BASIC handlers, the namespace is "/"
        __namespace = "/" if not_channel else self.namespace
        self.on_event(event_name, lambda msg: self.handle_event(msg, emit_name, callback, *callback_args), namespace=__namespace)

    def __register_basics_handlers(self) -> None:
        self.register_handler(True, 'connect', 'connected')
        self.register_handler(True, 'disconnect', 'disconnected')

    def handle_event(self, msg: Any, emit_name: str, callback = None, *calback_args) -> None:
        # By default, response is {True, DataReceived}
        # After can changes with the callback
        response = ResponseSocket(True, msg)

        # Call a intermediate function
        # Ever send the response reference to modify it's values, too send msg, data received!!!
        if callback:
            if calback_args:
                callback(msg, response, *calback_args)
            else:
                callback(msg, response)
        
        # Emit event to client, said that event is handled OK! or !OK
        emit(emit_name, response.to_dict(), namespace=self.namespace)