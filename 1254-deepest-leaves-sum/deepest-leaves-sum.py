# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        s=[]
        l=0
        c={}
        def deepestLeavesSum(root,s,l,c):

            if root==None:
                return 
            
            if l not in c.keys():
                c[l]=root.val
            else:
                c[l]+=root.val

            if root.left:
                deepestLeavesSum(root.left,s,l+1,c)

            if root.right:
                deepestLeavesSum(root.right,s,l+1,c)

            return c
            

            

        p= deepestLeavesSum(root,s,l,c)

        v=list(p.keys())

        return c[v[-1]]


            

