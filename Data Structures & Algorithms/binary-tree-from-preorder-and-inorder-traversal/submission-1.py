# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        pre order
        1,2,3,4

        in order
        2,1,3 4

        root=1
        leftmost=2 
        right=3
        right most=4
        """
        inorder_indices={value:i for i, value in enumerate(inorder)}
        self.preIdx=0
        def dfs(l,r):
            if l>r:
                return None
            root=preorder[self.preIdx]
            self.preIdx+=1
            mid=inorder_indices[root]
            root_node=TreeNode(root)
            root_node.left=dfs(l,mid-1)
            root_node.right=dfs(mid+1,r)
            return root_node
        return dfs(0,len(inorder)-1)


        
        