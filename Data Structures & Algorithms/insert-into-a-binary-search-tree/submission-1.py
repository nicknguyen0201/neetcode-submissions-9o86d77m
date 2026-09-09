# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        case 1
        insert to leaves
        case 2
        inser with only 1 child

        case 3
        insert with 2 children

        """
        def dfs(root):
            if not root:
                tmp=TreeNode(val)
                return tmp 
            if root.val<val:
                root.right=dfs(root.right)
               
            else:
                root.left=dfs(root.left)
            return root
               
        
        return dfs(root)