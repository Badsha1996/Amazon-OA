class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru = []



    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            self.cache[key] = value
        else:
            print(len(self.lru),self.capacity)
            if len(self.lru) == self.capacity:
                to_be_removed = self.lru[0]
                self.cache.pop(to_be_removed)
                self.cache[key] = value
                self.lru.remove(to_be_removed)
                self.lru.append(key)

            else:
                self.cache[key] = value
                self.lru.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)