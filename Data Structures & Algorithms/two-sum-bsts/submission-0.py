# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, ptr1: Optional[TreeNode], ptr2: Optional[TreeNode], target: int) -> bool:
        """
        assumptions

        Plan
        1 ptr each root
        target = ptr1+ptr2

        both ptr go right until exceed target

        base
        if not ptr1 or not ptr2:
            return False
        if ptr1+ptr2==targetL
            retyurn true

        if ptr+ptr2=17 <target:

            if 2sumbst(ptr1.right, ptr2,target):(10,5,18)
                return True

            return 2sumbst(ptr1,ptr2.right,target) (10,7,18)
        else:
            if 2sumbst(ptr1.left, ptr2,target):
                return True

            return 2sumbst(ptr1,ptr2.left,target)
        """
        if not ptr1 or not ptr2:
            return False
        if ptr1.val+ptr2.val==target:
            return True

        if ptr1.val+ptr2.val <target:

            if self.twoSumBSTs(ptr1.right, ptr2,target):
                return True
            return self.twoSumBSTs(ptr1,ptr2.right,target)
        else:
            if self.twoSumBSTs(ptr1.left, ptr2,target):
                return True
            return self.twoSumBSTs(ptr1,ptr2.left,target)