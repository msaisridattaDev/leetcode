# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leafSimilar(root,s) -> bool:

            if root.left==None and root.right==None:
                s+=[root.val]

            if root.left:
                leafSimilar(root.left,s)

            if root.right:
                leafSimilar(root.right,s)

            return s

        p=leafSimilar(root1,[])
        q=leafSimilar(root2,[])

        return p==q

            
