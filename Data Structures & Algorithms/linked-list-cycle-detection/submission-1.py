# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hare = head
        tor = head
        while hare and hare.next and hare.next.next:
            hare=hare.next.next
            tor=tor.next
            if hare.val==tor.val:
                return True
        return False