import os
from src.main import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4500))  # Fallback to 4500 if PORT is not set
    app.run(host="0.0.0.0", port=port)
