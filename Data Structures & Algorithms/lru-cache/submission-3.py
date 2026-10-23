class LRUCache:
    from collections import OrderedDict

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        # return m[key] if it exists, else -1
        # this key was used, so then we add it to end of linked list (deque)
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        
