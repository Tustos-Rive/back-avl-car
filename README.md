# ATC - Backend

Back-End (Server) for the "[avl_tree_car_front](https://github.com/tutosrive/avl_tree_car_front)" project


This project provides the logic and data structures for managing the **AVL Tree** and its **Nodes**.  
It is required for the front-end to work properly.

# Preview

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
