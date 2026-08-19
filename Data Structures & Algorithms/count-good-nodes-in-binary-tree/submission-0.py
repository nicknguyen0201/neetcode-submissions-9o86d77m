# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        do dfs(root, max)
        if max< root;
            res.append(root)
        """
        res=0
        def dfs(root, max_node):
            nonlocal res
            if not root:
                return
            if root.val>=max_node:
                res+=1
                max_node=root.val
            dfs(root.right,max_node)
            dfs(root.left,max_node)
        dfs(root,-float('inf'))
        return res
