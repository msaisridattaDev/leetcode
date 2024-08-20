# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        rev = True

        while q:
            count = len(q)
            nodes = []
            
            for _ in range(count):
                node = q.pop(0)
                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if nodes:
                res.append(nodes if rev else nodes[::-1])
            rev = not rev
        return res