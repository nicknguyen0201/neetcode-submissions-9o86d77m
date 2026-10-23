# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        understand:
        null root return null
        has to swap chilren and children of children
        if not root:
            return None
        if root:1 

            tmp = root.right 3 
            root.right=invertTree(root.left)2 4
            root.left=invertTree(tmp) 5

        """
        if not root:
            return None
        if root:
            tmp = root.right 
            root.right=self.invertTree(root.left)
            root.left=self.invertTree(tmp)
        return root