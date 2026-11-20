# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        highlevel overview
        find p q ancestor in bst
        return a node

        when you at a node, 5, 3<5<8 (candidate)
        you know how q and p relative to you
        I am ancestor

        example p = 1, q=4
        5>q and >p go left
        1<3<4
        ancestor = 3
        
        base case when you get to the middle value between qp, return that node
        base case II: 
        if root value == q or == p return root
        Pseudo code

        if q.val < root.val < p.val: 
            return root
        if p.val < root.val < q.val:
            return root
        if root.val == q.val or root.val == q.val:
            return root

        if root.val > p.val and root.val > q.val: 
            return lowestCommonAncestor(root.left, p, q)
        else:
            return lowestCommonAncestor(root.right, p, q)
        """
        if q.val < root.val < p.val: 
            return root
        if p.val < root.val < q.val:
            return root
        if root.val == q.val or root.val == p.val:
            return root

        if root.val > p.val and root.val > q.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)