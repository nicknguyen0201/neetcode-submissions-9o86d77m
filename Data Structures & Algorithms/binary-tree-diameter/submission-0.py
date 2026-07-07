# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        which node has the max (left +right ) depth

        if not root:
            return 0
        if not left not right 
            return 1
        return  (root.left) + (root.right)
        """
        res=0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left =dfs(root.left)
            right= dfs(root.right)
            res=max(res, left + right)
            return 1 + max(left,right)

        r=dfs(root)-1
        res=max(res,r)
        return res
