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
        Understand assumptions
        input:
        a single node in a graph need to clone

        output:
        the same node, but in a new deep copy graph

        1 - 2
        |   |
        3 - |

        dfs(node 1)

        mp{
        node 1: new node 1
        node 2: 2
        node 3: 3
        }
        node_clone.append(dfs(node 2))

                node_clone 2

                node clone 2.append(dfs(node1)
                node clone 2.append(dfs(node3))


                        node clone 3
                        node clone 3. append(dfs(1))
                        node clone 3. append(dfs(2))


        """
        #store old node to new node maping
        old_to_new=defaultdict(int)

        def dfs(node):
            if node in old_to_new: #the node in the old graph has been clone, return the copy
                return old_to_new[node]
            
            node_clone=Node(node.val)#make a new node

            old_to_new[node]=node_clone
            for nb in node.neighbors:
                #make a deep copy of neighbors list
                node_clone.neighbors.append(dfs(nb))
            return node_clone
        if not node:
            return None
        return dfs(node)
