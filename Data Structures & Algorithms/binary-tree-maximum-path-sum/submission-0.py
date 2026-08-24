# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        each node will report to higher up it's max sum
        each node will also consider the max_sum run thru itself, so try to calculate that also and put in res
        """
        res=root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left_sum=max(dfs(root.left),0)
            right_sum=max(dfs(root.right),0)
            res=max(res,root.val+left_sum+right_sum)
            return root.val+max(left_sum,right_sum)
        dfs(root)
        return res
