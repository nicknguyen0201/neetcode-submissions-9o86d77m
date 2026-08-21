# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow.next
        slow.next=None
        #reverting
        prev=None
        # 
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        #combining
        curr=head
        while prev:
            tmp1,tmp2=curr.next,prev.next
            curr.next=prev
            prev.next=tmp1
            curr,prev=tmp1,tmp2
        """
        2->4 6<-8
        c       p
        """

