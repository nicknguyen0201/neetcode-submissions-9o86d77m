# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        cur2=l2
        l3=ListNode()
        cur3=l3
        carry=0
        while cur1 or cur2 or carry:
            if cur1 and cur2:
                sum=cur1.val+cur2.val +carry
                carry=sum//10
                cur3.next=ListNode(sum%10,None)
                cur1=cur1.next
                cur2=cur2.next

            elif cur1==None and cur2:
                sum=cur2.val +carry
                carry=sum//10
                cur3.next=ListNode(sum%10,None)
                cur2=cur2.next
            elif cur2==None and cur1:
                sum=cur1.val +carry
                carry=sum//10
                cur3.next=ListNode(sum%10,None)
                cur1=cur1.next
            else:
                sum=carry
                carry=sum//10
                cur3.next=ListNode(sum,None)
            
            cur3=cur3.next
        return l3.next
