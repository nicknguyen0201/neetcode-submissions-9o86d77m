# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        U: remove nth node from the end
        the last node considered n=1
        
        P: identify last node, count back n
        you can't traverse backward in a linkedlist

        maintain 2 pointer 
        cur_left 
        cur_right
        diff left and r is n
        when right reach the end, delete left

        Input: head = [1,2], n = 1
                       l r

        Output: [1,2,3,5]
        Implement
        """

        l=r=head
        #r ptr maintain distance n with l
        for _ in range (n):
            r=r.next
        #edge case len ll =n
        if not r:
            head=head.next
            return head
        while r:
            if r.next ==None:
                break
            r=r.next
            l=l.next

        l.next=l.next.next
     

        return head