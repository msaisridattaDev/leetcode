# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        s1=[]
        s2=[]
        def getAllElements(root,s):

            if root.left:
                p=getAllElements(root.left,s)
                s=p
            s+=[root.val]
 
            if root.right:
                o=[]
                q=getAllElements(root.right,o)
                s+=q

            return s
        if root1:
            x=getAllElements(root1,s1)
        else:
            x=[]
        if root2:
            y=getAllElements(root2,s2)
        else:
            y=[]

        p1=0
        p2=0

        
        t=[]
        while(p1<=len(x)-1 and p2<=len(y)-1):

            if x[p1]<=y[p2]:
                t.append(x[p1])
                p1+=1
            else:
                t.append(y[p2])
                p2+=1

        #print(t,p1,p2)

        if p2==len(y):
            t+=x[p1::]
            #print(t)
        elif p1==len(x):
            t+=y[p2::]

        return t





