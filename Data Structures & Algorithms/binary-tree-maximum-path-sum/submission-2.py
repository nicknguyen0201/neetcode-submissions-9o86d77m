# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Plan:
        
        res=max(left_sub tree, right sub tree)
        return max(right sub tree and left sub tree's sum)+root value

        """
        res=root.val
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left_tree=dfs(root.left)
            if left_tree<0:
                left_tree=0
            right_tree=dfs(root.right)
            if right_tree<0:
                right_tree=0
            res=max(res,left_tree+right_tree+root.val)
            return root.val+max(left_tree, right_tree)
        tmp=dfs(root)
        return max(res,tmp)