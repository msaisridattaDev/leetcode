# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        k=[]

        m=[]

        def pathSum(root,t,s,k,m):

            if not root:
                return 


            if root.left==None and root.right==None:
                if t==s+root.val:
                    k+=[root.val]
                    m+=[k]
            else:
                pathSum(root.left,t,s+root.val,k+[root.val],m)
                pathSum(root.right,t,s+root.val,k+[root.val],m)
        
        pathSum(root,targetSum,0,k,m)
        print(m)
        return m


            
