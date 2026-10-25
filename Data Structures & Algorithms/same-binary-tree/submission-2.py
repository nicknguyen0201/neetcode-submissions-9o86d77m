# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        check at every level if not match return false
        """
        # 3 base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        #p=q is true
        if not self.isSameTree(p.left,q.left):
            return False
        if not self.isSameTree(p.right,q.right):
            return False
        return True
        