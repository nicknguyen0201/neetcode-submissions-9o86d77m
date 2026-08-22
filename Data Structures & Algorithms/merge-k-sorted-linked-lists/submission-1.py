# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import  heappush, heappop
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        use min heap size k
        add(val, reference to the node)

        """
        h=[]
        dummy=ListNode()
        tmp=dummy
        tie_break=0
        for i in range(len(lists)):
            if lists[i]:
                heappush(h,(lists[i].val,tie_break,lists[i]))
                tie_break+=1
        while h:
            val,_,curr=heappop(h)
            tmp.next=ListNode(val)
            tmp=tmp.next
            if curr.next:
                heappush(h,(curr.next.val,tie_break,curr.next))
                tie_break+=1
        return dummy.next

        