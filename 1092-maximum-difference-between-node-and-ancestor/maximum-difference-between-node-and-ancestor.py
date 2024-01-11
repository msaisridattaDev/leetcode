# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        m=-sys.maxsize
        n=sys.maxsize
        a=0


        def maxAncestorDiff(root,m,n,a):

            if root.val > m:
                m=root.val
            
            if root.val < n:
                n=root.val


            if abs(root.val-m)>a:
                
                a=abs(root.val-m)
                

            if abs(root.val-n)>a:
                a=abs(root.val-n)
               
            
        
            if root.left:
               v=maxAncestorDiff(root.left,m,n,a)
               if v>a:
                   a=v
            
            if root.right:
               u= maxAncestorDiff(root.right,m,n,a)
               if u>a:
                   a=u


            return a

        p= maxAncestorDiff(root,m,n,a)

        return p


