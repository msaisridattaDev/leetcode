# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        c=1
        j=[]

        if not root:
            return 0
        def minDepth2(root,c,j):

            if not root:
                return

            minDepth2(root.left,c+1,j)
            minDepth2(root.right,c+1,j)

            if not root.right and not root.left:
                j+=[c]
            return
        
        minDepth2(root,c,j)
        print(j)
        return min(j)


        