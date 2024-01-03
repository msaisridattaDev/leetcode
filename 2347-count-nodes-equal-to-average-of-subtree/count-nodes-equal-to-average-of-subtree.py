# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        o=0
        k=[]
        def averageOfSubtree(root,k,o) -> int:

            if root==None:
                return k,0
            
            p,x=averageOfSubtree(root.left,k,o)
            o=x 
            q,y=averageOfSubtree(root.right,k,o)
            o+=y

            avg=int((sum(p)+sum(q)+root.val)/(len(p)+len(q)+1))
            if avg==root.val:
                print(root.val)
                o+=1
                return [k+[root.val]+p+q,o]
            else:
                return [k+[root.val]+p+q,o]

        f,g=averageOfSubtree(root,k,o)

        print(f,g)
        return g

