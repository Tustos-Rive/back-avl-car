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