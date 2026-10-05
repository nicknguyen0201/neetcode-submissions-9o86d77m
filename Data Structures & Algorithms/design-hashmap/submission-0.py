class MyHashMap:

    def __init__(self):
        self.mp=defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.mp[key]=value

    def get(self, key: int) -> int:
        return self.mp[key]if key in self.mp else -1

    def remove(self, key: int) -> None:
        if key in self.mp:
            del self.mp[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)