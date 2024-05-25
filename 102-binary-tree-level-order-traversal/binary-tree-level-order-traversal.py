# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[root]
        if l[0] is not  None:
            t=[]
            t=t+[[root.val]]
        else:
            t=[]
        y=[]
        while len(l)!=0:
            if l[0]!=None:
                if (l[0].left!=None):
                    y.append(l[0].left)
                if (l[0].right!=None):
                    y.append(l[0].right)
            l.pop(0)
            if len(l)==0:
                for i in range(len(y)):
                    l.append(y[i])

                    y[i]=y[i].val

                if y:
                    t=t+[y]
                y=[]

        return t
        
        
        




