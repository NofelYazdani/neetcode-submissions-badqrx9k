class LRUCache:

    def __init__(self, capacity: int):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.array:
            return -1
        self.array.move_to_end(key)
        return self.array[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.array:
            self.array.move_to_end(key)
        self.array[key] = value
        if len(self.array) > self.capacity:
            self.array.popitem(last=False)
        
        
        