# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        m=[]
        def dfs(root,k,m):

            if not root:
                return

            dfs(root.left,k,m)
            m.append(root.val)
            dfs(root.right,k,m)
            return

        dfs(root,k,m)


        return m[k-1]
        




        