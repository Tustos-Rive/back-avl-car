class MainRoute:
    def __init__(self, app, jsonify):
        self.app = app
        self.jsonify = jsonify

        self.__register_routes()

    def __register_routes(self):
        self.app.add_url_rule("/", view_func=self.home)

    def home(self):
        return self.jsonify({'message':'Hello from flask'})