# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q=collections.deque()
        if root:
            q.append(root)

        res=[]

        while q:

            l=len(q)

            level=[]

            for i in range(l):
                
                p=q.popleft()
                
                if p:
                    level.append(p.val)
                    q.append(p.left)
                    q.append(p.right)

            if level:
                res+=[sum(level)/len(level)]
        
        return res


