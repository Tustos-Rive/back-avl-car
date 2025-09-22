from typing import Any
from flask import Flask

class Router:
    def __init__(self, app: Flask, jsonify: Any) -> None:
        self.app = app
        self.jsonify = jsonify

    def register_routes(self, url: str, handler: Any) -> None:
        """Add a rule/route rule to Flask.app
        
        Args:
            `url:str`: The URL that handle the rule
            `handler:Any`: The callback/function that work it!
        """
        self.app.add_url_rule(url, view_func=handler, provide_automatic_options=True)
        # Something times can NOT remember :/ put "{url}/"
        self.app.add_url_rule(f'{url}/', view_func=handler, provide_automatic_options=True)