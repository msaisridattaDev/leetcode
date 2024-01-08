# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        s=[]
        def rangeSumBST2(root,low,high,s):

            if not root:
                return 0

            if  root.val > high:
                rangeSumBST2(root.left,low,high,s)

            elif root.val < low:
                rangeSumBST2(root.right,low,high,s)

            elif low <= root.val <= high:
                #print(root.val)
                s.append(root.val)
                rangeSumBST2(root.left,low,high,s)
                rangeSumBST2(root.right,low,high,s)

            return s

        return sum(rangeSumBST2(root,low,high,s))




        