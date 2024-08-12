# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            path=[]

            def lowestCommonAncestor(root,k):

                if root.left ==None and root.right==None:

                    if root==k:
                        path.append(root)
                        return True
                    else:
                        return False

                path.append(root)

                if root==k:
                    return True

                if (root.left and lowestCommonAncestor(root.left,k)) or (root.right and lowestCommonAncestor(root.right,k)):
                    return True

                path.pop()

                return False

            lowestCommonAncestor(root,p)
            path1=path
            path=[]
            lowestCommonAncestor(root,q)
            path2=path

            p1=0
            p2=0

            
            while(p1<=len(path1)-1 and p2<=len(path2)-1):
                #print(path1[p1],"----\n",path2[p2],"****\n")

                if path1[p1]==path2[p2]:

                    p1+=1
                    p2+=1
                else:
                    if p1!=0:
                        return path1[p1-1]
                    return path1[p1]

            return path1[p1-1]







        