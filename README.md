# ATC - Backend

> [!NOTE]
> See the final note

Back-End (Server) for the "[avl_tree_car_front](https://github.com/tutosrive/avl_tree_car_front)" project


This project provides the logic and data structures for managing the **AVL Tree** and its **Nodes**.  
It is required for the front-end to work properly.

# Preview ([Front-End View](https://github.com/tutosrive/avl_tree_car_front))

https://github.com/user-attachments/assets/e3291ff1-c863-4c9f-ba7e-fe87221e11a6

# How to Use?

> [!IMPORTANT]
> This project is the server/backend for [ATC Frontend](https://github.com/tutosrive/avl_tree_car_front).  
> Please set up this backend before using the frontend!

1. Download/clone this repository
    ```shell
    git clone https://github.com/tutosrive/avl_tree_car.git
    ```
2. Change directory to the cloned folder
    ```shell
    cd avl_tree_car
    ```
3. Ensure you have Python installed (100% Python project)
4. (Optional) Set up a virtual environment (You can use [InitVenv](https://github.com/Dev2Forge/Init-Venv)
    ```shell
    python -m venv .venv
    source .venv/bin/activate

    # On Windows:
    .venv\Scripts\activate
    ```
5. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```
6. Run the server
    ```shell
    python run.py

    # ALternative
    py run.py
    ```
7. Make sure the server is running without errors!

Your frontend can now connect to this backend for all AVL Tree operations.

> [!NOTE]
> Yo can use this JSON test.
> [configs.json](https://github.com/user-attachments/files/22607038/configs.json)

```json
{
  "configs": {
    "total_distance": 1000,
    "velocity": 10,
    "ms_update": 200,
    "jump_height": 40,
    "car_colors": ["#F54927", "#8F2510", "#BD2C11"]
  },
  "obstacles": [
    { "x": 100, "y": 20, "type": "rock" },
    { "x": 760, "y": 10, "type": "trunk" },
    { "x": 990, "y": 50, "type": "nail" },
    { "x": 560, "y": 12, "type": "cone" },
    { "x": 780, "y": 15, "type": "tire" },
    { "x": 360, "y": 45, "type": "tree" },
    { "x": 550, "y": 20, "type": "chair" },
    { "x": 140, "y": 10, "type": "person" }
  ]
}
```

