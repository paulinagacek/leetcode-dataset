from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
			# if we touch a key to return its value, we need to add it 
			# to the end of the least recently used items in our cache
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key already exists - if yes, move item to end and update the value
        if key in self.cache:
            self.cache.move_to_end(key)
        # if cache is full, remove least recent item (first value in OrderedDict)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
		# update/add value
        self.cache[key] = value