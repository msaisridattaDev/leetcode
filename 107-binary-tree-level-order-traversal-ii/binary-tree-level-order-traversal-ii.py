# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=[]
        q+=[root]
        m=[]
        t=[]
        c=[]
        while(len(q)!=0):
            p=q.pop(0)
            if  p.left:
                c+=[p.left]
            if  p.right: 
                c+=[p.right]
            
            t+=[p.val]
            if (len(q)==0):
                m+=[t]
                q=copy.deepcopy(c)
                #print(q)
                c=[]
                t=[]

        for i in range(len(m)):
            c+=[m.pop()]

        return c

                
            



        