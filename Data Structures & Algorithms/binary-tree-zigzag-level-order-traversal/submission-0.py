# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Plan:
        do some bfs
        append root
        when process next level alternate
        when iter child to put to queue
        level 0 left right
        level 1 right left

        """
        if not root:
            return []
        q=deque([root])
        output=[]
        right_left=True
        while q:
            len_level=len(q)
            tmp=[0]*len_level
            for i in range(len_level):
                node=q.popleft()
                index =  i if right_left else len_level -1-i
                tmp[index] = node.val
                for child in [node.left,node.right]:
                    if child:
                        q.append(child)
            right_left=not right_left
            output.append(tmp)
            
        return output
