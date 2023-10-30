# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        m=[]
        k=[]
        def sumNumbers2(root,k,m):

            if root.left==None and root.right==None:
                k+=[str(root.val)]
                m+=["".join(k)]
                return m


            if root.left!=None:
                sumNumbers2(root.left,k+[str(root.val)],m)

            if root.right!=None:
                sumNumbers2(root.right,k+[str(root.val)],m)

            return m

            
        sumNumbers2(root,k,m)
        
        s=0
        for i in m:
            s+=int(i)

        return s




        