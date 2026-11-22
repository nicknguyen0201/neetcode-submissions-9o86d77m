# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents={root: None}# child -> parent 

        queue = deque([root])

        while queue and(q not in parents or p not in parents):# while queue not empty, early stop when we have built both pq parents map
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node

        if p not in parents or q not in parents:
            return None
        
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p=parents[p]

        while q:
            if q in p_ancestors:
                return q
            q = parents[q]
        return None
        
            
            