# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
           
            This can be done recursively?

            at each level try combining 2 number
            if null l1, l2 carry=0
                return null
            else:
                if l1:
                    return node l1+carry
                else if l2:
                    l2+carry
                else:
                    node(carry)
            sum = sum+carry
            if  sum > = 10:
                carry = sum/10
            make a new node with sum%10
            recurse on ( list1, list 2, carry)
        """
        def add(curr1: Optional[ListNode], curr2: Optional[ListNode], carry: int):
            #base
            if curr1 == None and curr2 == None and carry == 0:
                    return None

            val1 = curr1.val if curr1 else 0#3
            val2 = curr2.val if curr2 else 0#0

            sum = val1 + val2 + carry #3
            carry = sum // 10 #0
            new_val = sum % 10 #3

            node = ListNode(new_val)
            node.next = add(curr1.next if curr1 else None, curr2.next if curr2 else None, carry)
            return node
        """
         3 2 1 7 + 7 7 7

            7-1-2-3
            7-7-7

            4-9-9-3

            carry = 0
            4->9->9->3->
        """
        return add(l1,l2,0)
