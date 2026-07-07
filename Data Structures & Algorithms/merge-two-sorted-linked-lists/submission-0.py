# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        list1 = [1,2,4], list2 = [1,3,5]
        
        """
        
        dummy=node=ListNode()
        curr1,curr2=list1,list2

        while curr1 and curr2:
            if curr1.val>curr2.val:
                node.next=curr2
                node=node.next
                curr2=curr2.next
            else:
                node.next=curr1
                node=node.next
                curr1=curr1.next
        if not curr1:
            node.next=curr2
        else:
            node.next=curr1
        return dummy.next
                


            

        
