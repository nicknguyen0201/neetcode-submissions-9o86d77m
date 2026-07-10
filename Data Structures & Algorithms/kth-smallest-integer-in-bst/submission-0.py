# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        at root calcualte how small you are
        leftmost is the 1st smallest
        right most is the nth smalles, 
        return root when root=k
        """
        res=[]

        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k-1]