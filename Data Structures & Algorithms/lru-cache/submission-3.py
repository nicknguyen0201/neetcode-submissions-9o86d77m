
class Node:
    def __init__(self, key,val):
        self.prev=None
        self.next=None
        self.key=key
        self.val=val

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity
        self.start=Node(-1,-1)
        self.end=Node(-1,-1)
        self.end.prev=self.start
        self.start.next=self.end

        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev = node.prev
    def insert(self, node):
        self.end.prev.next=node
        node.prev=self.end.prev
        self.end.prev=node
        node.next=self.end
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val

            self.remove(self.cache[key])
            self.cache[key]=Node(key,value)

            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])
        else:
            if len(self.cache)<self.cap:
                self.cache[key]=Node(key,value)
                self.insert(self.cache[key])
            else:
                old_key=self.start.next.key
                self.remove(self.start.next)
                del self.cache[old_key]
                self.cache[key]=Node(key,value)
                self.insert(self.cache[key])
        
                
                

       



