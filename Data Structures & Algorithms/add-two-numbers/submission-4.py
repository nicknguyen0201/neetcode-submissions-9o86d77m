# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        high lev overview
        2 list head
        return int

        1 - 9
        9
        0-0-1 
        100

        def add(l1,l2,carry)None,None, 0
            #base case
            if l2 = None and l2 = None and carry =0
                return []
            l1_val = 0 if not l1 else l1.val #1
            l2_val = 0 if not l2 else l2.val #9

            l1 + l2 + carry >=10:
                new carry = l1 + l2 + carry //10 #0
            res = l1 + l2 + carry % 10 #1
            return [res]+ add(None if not l1 else l1.next, l2.next, new_carry)

            return [0]+[0]+[1]
        """
        def add(l1,l2,carry):#8,None, 0
            #base case
            if l2 == None and l1 == None and carry == 0:
                return None
            l1_val = 0 if not l1 else l1.val #8
            l2_val = 0 if not l2 else l2.val #0

            remain = (l1_val + l2_val + carry) % 10 #8

            if l1_val + l2_val + carry >= 10:
                carry = (l1_val + l2_val + carry) // 10 #0
            else:
                #clear carry 
                carry = 0
            node = ListNode(remain) #8
            node.next = add(None if not l1 else l1.next, None if not l2 else l2.next, carry)
            return node
        return add(l1,l2,0)
