# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:

        def isValidBST2(self, root,l) -> bool:

            if not root:
                return True

            s= range(l[0],l[1])

            if ( root.val in s):

                if (self.isValidBST2(root.right,[root.val+1,l[1]]) and self.isValidBST2(root.left,[l[0],root.val])):
                    print("valid for ",root.val,"\n",l)
                    return True
                else:
                    print("invalid for ",root.val,"\n",l)
                    return False
            else:
                print("invalid for ",root.val,"\n outer if",l)
                return False
            






        def isValidBST(self, root: Optional[TreeNode]) -> bool:

                return (self.isValidBST2(root,[-sys.maxsize,sys.maxsize]))

        
