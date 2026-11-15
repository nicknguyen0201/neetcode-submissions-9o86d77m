# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        overview
        use recursive? to delte
        case 1:
            delete leaf
        case 2: delete non leaf:
            - find replacement: go right and go all the way left to find a leaf replacememnt
        if leaf and val == key: return None
        if val == key
            node = find_replacement()
            deleteNode(node)
            return node
        #noremal recursion
        if val > key: go left
        else: go right
        """
        if not root:
            return None
        if root.val > key: #smaller, go left
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:# this is the exact node
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            #return None implicitly if this is a leaf node

            # here mean the root has both left and right
            sucessor = root.right
            parent = root
            while sucessor.left:
                parent = sucessor
                sucessor = sucessor.left
                
            #we know we are at some leaf node
            if parent is not root:
                parent.left = sucessor.right #weird edge case when leftmost node has a right child
                sucessor.right = root.right#promote to root
            sucessor.left = root.left
            return sucessor
        return root
            

       

    


        