# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        high level overview
        list1 and list2 recurse
        each level do a compare,
        
        have a temporary reference
        then move head to right thing and
        tmp ref.next = recurse on the list1,list2

        #base
        one list run out use the entire other
        return the not empty lsit 

        both list run out at the same time
        return None

        curr=list1
        if list1.val <= lst2.val:
            
            list1=list1.next
            curr.next = recurse(list1,list2)
        else:
        return curr
        
        curr = 1 -> merge2list(2,1)
        list1 = 2
        list2 = 1

            curr=1 ->merge(2,2)
            l1=2
            l2=2
        """
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        merged_node = list1#1
        if list1.val <= list2.val:
            list1 = list1.next
            merged_node.next = self.mergeTwoLists(list1,list2)
        else:
            merged_node = list2
            list2 = list2.next
            merged_node.next = self.mergeTwoLists(list1,list2)
        return merged_node
        

