# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            left        r
        0- >  1 ->  2 -> 3 ->None    4 -> 5
        """
        dummy=ListNode(0,head)
        prevleft=dummy
        curr=head
        for _ in range(left-1):
            prevleft=curr
            curr=curr.next
        prev=None
        for _ in range(right-left+1):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        prevleft.next.next=curr
        prevleft.next=prev
        return dummy.next
        