from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)  # Remove the key to update its position
            self.cache[key] = value  # Re-insert the key to mark it as recently used
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)  # Remove the key to update its position
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove the first item (least recently used)
        self.cache[key] = value  # Insert the key-value pair as the most recently used
