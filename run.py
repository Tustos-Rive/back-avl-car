import os
from src.main import Main

if __name__ == "__main__":
    main = Main('*')
    port = int(os.getenv("PORT", 4500))  # Fallback to 4500 if PORT is not set
    main.socketio.run(host="0.0.0.0", port=port)
