# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(res,root):
            if not root:
                res.append('N')
                return 
            res.append(str(root.val))
            dfs(res,root.left)
            dfs(res,root.right)
        dfs(res,root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.preIdx=0
        data=data.split(',')
        def dfs():
            
            root_val=data[self.preIdx]
            if root_val=='N':
                self.preIdx+=1
                return None
            root=TreeNode(root_val)
            self.preIdx+=1
            root.left=dfs()
            root.right=dfs()
            return root
        
        return dfs()




