# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,max_val,min_val):
            if not root:
                return True
            if not (min_val<root.val<max_val):
                return False
            return check(root.left,root.val,min_val) and check(root.right,max_val,root.val )
        return check(root,float('infinity'),-float('infinity'))