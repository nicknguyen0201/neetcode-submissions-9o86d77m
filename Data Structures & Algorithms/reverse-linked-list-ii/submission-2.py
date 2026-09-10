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
        d.    h                   nextnode
        prev
            sub head
                    sub tail
        None<-1   <-2   3 ->None
                    prev
                        curr
                            nextndoe
        """
        def reverse(head):
            prev=None
            curr=head
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        subhead=prev.next
        subtail=subhead
        for _ in range(right-left):
            subtail=subtail.next
        next_node=subtail.next
        subtail.next=None
        reverse(subhead)
        subhead.next=next_node
        prev.next=subtail
        return dummy.next

