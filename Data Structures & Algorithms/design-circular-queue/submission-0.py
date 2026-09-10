class ListNode:
    def __init__(self, val=-1, next=None ):
        self.val=val
        self.next=next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size=0
        self.cap=k
        self.head=None
        self.tail=self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head=ListNode(value)
            self.tail=self.head
        else:
            self.tail.next=ListNode(value,self.head)
            self.tail=self.tail.next
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head=self.head.next
        self.tail.next=self.head
        self.size-=1
        return True
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.head==None

    def isFull(self) -> bool:
        return self.size==self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()