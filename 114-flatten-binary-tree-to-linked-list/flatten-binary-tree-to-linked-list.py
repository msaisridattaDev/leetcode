# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:

        if not root:
            return None,None
        else:
            nxt,ptr2=self.flatten(root.right)
            #print(nxt)
            smtng,ptr=self.flatten(root.left)
            #print(root.right)
            if nxt and smtng:
                ptr.right=nxt
                root.left=None
                root.right=smtng
                ptr=ptr2
                print(root)
            elif nxt:
                ptr=ptr2
                root.left=None
            elif smtng:
                root.right=smtng
                root.left=None
                ptr=ptr
            else:
                ptr=root
                print(ptr,root)
            return root,ptr
       

      
        