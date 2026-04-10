class LRUCache:
    """
    doubly ll 
    hash map that store key, pointer to dll object?
    and the head and tail
    we add to head for new page
    remove from tail for old page 
    """

    def __init__(self, capacity: int):
        self.cache=OrderedDict()
        self.cap=capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            
            self.cache[key]=value
            self.cache.move_to_end(key)
        else:
            if len(self.cache)<self.cap:
                pass
            else:
                self.cache.popitem(last=False)
            self.cache[key]=value
            self.cache.move_to_end(key)
        
