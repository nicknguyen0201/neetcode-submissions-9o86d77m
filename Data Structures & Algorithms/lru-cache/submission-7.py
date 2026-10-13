class DLL:
    def __init__(self,k,value,l=None,r=None):
        self.key=k
        self.val=value
        self.prev=l
        self.next=r
class LRUCache:
    def __init__(self, capacity: int):
        self.cache=OrderedDict()
        self.cap=capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.cache.move_to_end(key)
        elif len(self.cache)<self.cap:
            self.cache[key]=value
        else:
            self.cache.popitem(last=False)
            self.cache[key]=value
        
    """
    hashmap to keep track of key
    key in hashmap point to a DDL object
    the head of the ddl store lru, tail store mru

    head -> -1(dummy) ->
             tail
    
    def __init__(self, capacity: int):
        self.head=DLL(-1,-1)
        self.tail=DLL(-1,-1)
        self.tail.prev=self.head
        self.head.next=self.tail

        self.mp = {}
        self.cap=capacity
        self.usage=0
    def get(self, key: int) -> int:
        if key in self.mp:
            self.append_end(self.mp[key])
            return self.mp[key].val
        return -1
    def insert(self,node):
        tmp = self.tail.prev
        tmp.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = tmp

    def append_end(self,node):
        left_neighbor = node.prev
        right_neighbor = node.next

        left_neighbor.next = right_neighbor
        right_neighbor.prev = left_neighbor
        self.insert(node)
        

    def remove(self):
        node=self.head.next
        right_neighbor=node.next

        self.head.next=right_neighbor
        right_neighbor.prev=self.head

    def put(self, key: int, value: int) -> None:
        
        if key in self.mp:
            self.mp[key].val=value
            
            if self.tail.val!=value:
                self.append_end(self.mp[key])
        else:
            self.usage+=1
            if self.usage<=self.cap:
                self.mp[key]=DLL(key,value)
                self.insert(self.mp[key])

            else:#eviction
                lru_key=self.head.next.key
                self.remove()
                del self.mp[lru_key]
                self.mp[key]=DLL(key,value)
                self.insert(self.mp[key])
    """

            
