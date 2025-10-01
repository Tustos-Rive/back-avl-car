from src.main import Main
from random import randint

from src.models.obstacle import Obstacle
from src.models.tree import AVLTree
from src.utils.others_utils import Utils

if __name__ == "__main__":
    import sys
    if "--serve" in sys.argv:
        main.socketio.run(main.app, host="0.0.0.0", port=4500, debug=True, allow_unsafe_werkzeug=True)
    else:
        print("Build mode: not starting Flask server")
