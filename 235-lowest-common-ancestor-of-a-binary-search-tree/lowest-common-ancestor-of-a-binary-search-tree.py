# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':



        def dfs(root,p,l):

            if  p.val < root .val:
                l.append(root)
                return dfs(root.left,p,l)


            elif p.val == root .val:
                l.append(root)
                return l

            else:
                l.append(root)
                return dfs(root.right,p,l)

        u=dfs(root,p,[])
        v=dfs(root,q,[])


        p1=0
        p2=0

        while(p1<=len(u)-1 and p2<=len(v)-1):

            if u[p1].val==v[p2].val:
                print(u[p1].val,v[p2].val)
                p1+=1
                p2+=1
            else:
                break
        g=min(p1-1,p2-1)

        return u[g]