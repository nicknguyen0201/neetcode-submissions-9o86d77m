# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root,can_rob):
            if not root:
                return 0
            if not can_rob:
                return dfs(root.left,True)+dfs(root.right,True)
            pick_root=dfs(root.left,False)+dfs(root.right,False)+root.val
            pick_children=dfs(root.left,True)+dfs(root.right,True)
            return max(pick_root,pick_children)
        return dfs(root,True)