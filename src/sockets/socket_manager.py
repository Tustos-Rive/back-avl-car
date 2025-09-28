from typing import Any
from flask import Flask
from flask_socketio import SocketIO, emit
from src.models.responses import ResponseSocket

class SocketManager(SocketIO):
    # def __init__(self, socketio: SocketIO, app: Flask):
    def __init__(self, app: Flask, cors: str, namespace: str = "/") -> None:
        super().__init__(app, cors_allowed_origins=cors)

        # Channel
        self.namespace = namespace

        # Register the basics handlers (Connect & Disconnect)
        self.__register_basics_handlers()

    def register_handler(self, not_channel = True, event_name: str = '', emit_name: str = '', callback: Any | None = None, need_control_emit: bool = False, *callback_args):
        # Call the handle_event()
        # When are the BASIC handlers, the namespace is "/"
        __namespace = "/" if not_channel else self.namespace
        self.on_event(event_name, lambda msg: self.handle_event(msg, emit_name, callback, need_control_emit, *callback_args), namespace=__namespace)

    def __register_basics_handlers(self) -> None:
        self.register_handler(True, 'connect', 'connected', self.__on_connect, True)
        self.register_handler(True, 'disconnect', 'disconnected', self.__on_disconnect, True)

    def __on_connect(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        response.msg = 'The Socket is Connected, ready to use!'
        emit(emit_name, response.to_dict(), namespace=namespace)

    def __on_disconnect(self, msg: Any, response: ResponseSocket, emit_name: str, namespace: str) -> None:
        response.msg = 'The has been disconneted!'
        emit(emit_name, response.to_dict(), namespace=namespace)
        # Stop socket!
        self.stop()

    def handle_event(self, msg: Any, emit_name: str, callback: Any | None = None, need_control_emit: bool = False, *calback_args) -> None:
        # By default, response is {True, DataReceived, Eventname -> channel/endpoint, EmitName -> Endpoint}
        # After can changes with the callback
        response = ResponseSocket(True, msg)

        # Call a intermediate function
        # Ever send the response reference to modify it's values, too send msg, data received!!!
        # Callback said that need the control of EMIT method
        if callback and calback_args and need_control_emit:
            # emit + args
            callback(msg, response, emit_name, self.namespace, *calback_args)
        elif callback and calback_args and not need_control_emit:
            # args
            callback(msg, response, *calback_args)
        elif callback and need_control_emit:
            # emit
            callback(msg, response, emit_name, self.namespace)
        elif callback:
            # nothing additional
            callback(msg, response)
        
        if not need_control_emit:
            # Emit event to client, said that event is handled OK! or !OK
            emit(emit_name, response.to_dict(), namespace=self.namespace)