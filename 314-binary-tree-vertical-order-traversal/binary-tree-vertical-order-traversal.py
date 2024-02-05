# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        t={}
        col,row=0,0

        if not root:
            return root
    
        def verticalTraversal2(root,t,col,row):
            if not root:
                return
            try:
                if t[(col,row)]: 
                    t[(col,row)]+=[root.val]
            except:
                    t[(col,row)]=[root.val]

            verticalTraversal2(root.left,t,col-1,row+1)
            verticalTraversal2(root.right,t,col+1,row+1)

        verticalTraversal2(root,t,col,row)
        
        e=OrderedDict(sorted(t.items()))
        y=list(e.items())
   

        p=y[0][0]
        a=[]
        b=[]
        for k,v in e.items():
            
            
            m=k[0]

            if m==p:
                b.extend(v)
            else:
                a.append(b)
                b=[]
                p=m
                b.extend(v)
                
        a.append(b)
        return a[1::]

        

            

