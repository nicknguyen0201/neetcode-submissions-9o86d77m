# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: self-first, self, left, right
        in order: left, self, right

        Understand:
        the fist node in pre-order is always the root
        root=preorder[0]
        the mid index = 
        index of root in inorder arr

        the second node in po is always the left sub tree, if we have left sub tree
        left subtree for preorder [1:1+mid]
                         in order [:mid]
        right subtree for preorder[mid+1:]
                         inorder [mid+1:]

        """
        if not preorder: 
            return None
        root=preorder[0]
        mid = inorder.index(root)
        node = TreeNode(root)
        node.left=self.buildTree(preorder[1:1+mid],inorder [:mid])
        node.right = self.buildTree(preorder[mid+1:],
                         inorder[mid+1:])
        return node