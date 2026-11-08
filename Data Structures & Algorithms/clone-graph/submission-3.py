"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        should be a simple recursion problem because 
        start a root object, and list

        maintain a visited set

        we need to traverse the neighbor list
        
        then add the neighbor to list while also recurse on the neighbor
        root = Node(node.val)
        for i in range(len(node.neighbors)):
            root.neighbors.append(cloneGraph(node.neighbor[i])
        return root
        """
        old_to_new={}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            cloned_root = Node(node.val)
            old_to_new[node] = cloned_root
            for i in range(len(node.neighbors)):  
                cloned_root.neighbors.append(dfs(node.neighbors[i]))
            return cloned_root
        return dfs(node) if node else None
