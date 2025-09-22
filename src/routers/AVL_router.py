from flask import Flask


class AVLRouter:
    def __init__(self, app: Flask):
        self.app = app