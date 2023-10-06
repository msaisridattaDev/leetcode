# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        flag=False

        if not root:
            return False
        def dfs(root,t,s) -> bool:

            if not root:
                return 

            if root.left==None and root.right==None:
                if t==s+root.val:
                    return True
                return False
            else:
                return dfs(root.right,t,s+root.val) or dfs(root.left,t,s+root.val)
            
   
        if dfs(root,targetSum,0) :
            return True
        else:
            return False
        