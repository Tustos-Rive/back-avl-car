from src.models.node import Node

class Utils:
    @classmethod
    def extract_tree_childs(cls, tree: Node) -> dict | None:
        def wrapper(current: Node):
            __response: dict | None = None
            if current:
                # Response re-initialize just for each child, but thanks recursive
                # Response in first ambient is OK, and is not removed or overwrited!
                __response = {'id': current.value.id}

                # Current node childs
                childs = []

                if current.left:
                    # Call recursively, until arrive to a leaft node!
                    childs.append(wrapper(current.left))
                if current.right:
                    childs.append(wrapper(current.right))
                
                # If the current node have childs, add it!
                if len(childs) > 0:
                    # __response['childs'] = childs
                    __response['children'] = childs
            
            return __response
        # Is not a decorator, because not return a function, just return a dict DATA!
        return wrapper(tree)

    @classmethod
    def validate_json_configs(cls, data: dict) -> dict | None:
        response: dict = {}
        if not data:
            return {'error': 'Missing data...'}

        need_keys_configs = ['total_distance', 'jump_height']
        need_keys_obstacles = ['x', 'y', 'type']

        # Validate configs section
        if not data.get('configs'):
            return {'error': "Missing 'configs' section"}

        # Check required config keys
        missing_configs = [key for key in need_keys_configs if key not in data['configs']]
        if missing_configs:
            return {'error': f"Missing required config keys: {', '.join(missing_configs)}"}

        # Validate obstacles section
        if not data.get('obstacles'):
            return {'error': "Missing 'obstacles' section"}

        if not isinstance(data['obstacles'], list):
            return {'error': "'obstacles' must be a list"}

        # Check each obstacle has required keys
        for idx, obstacle in enumerate(data['obstacles']):
            missing_keys = [key for key in need_keys_obstacles if key not in obstacle]
            if missing_keys:
                return {'error': f"Obstacle at index {idx} is missing keys: {', '.join(missing_keys)}"}

        # If all validations pass, return the data
        return data