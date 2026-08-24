# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
        
        dummy=ListNode(-1,head)
        group_prev=dummy
        while True:
            kth=get_kth(group_prev,k)
            if not kth:
                break
            prev=group_next=kth.next
            curr=group_prev.next
            while curr!=group_next:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp=group_prev.next
            group_prev.next=kth

            
            group_prev=tmp
        return dummy.next
                

                