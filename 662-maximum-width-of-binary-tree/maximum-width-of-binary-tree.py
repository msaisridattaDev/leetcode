# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q=[]
        u=0
        v=0
        if root:
            q.append(root)

        res=[]
        b=0
        while q:

            l=len(q)
            
        
            u=0
            v=0
            h=[]
            

            for i in range(l):

                
                p=q.pop(0)
                
            
            
                if type(p)==TreeNode:

                  

    
                    u+=v
                    u+=1
                    v=0
                    
                    h.append(u)
                    if p.left:
                        q.append(p.left)
                    else:
                        q.append("1")

                    if p.right:
                        q.append(p.right)
                    else:
                        q.append("1")

                elif type(p)==str:

                    if u>0:
                        v+=int(p)
                        q.append(str(int(p)*2))


          

            if b <u:
                b=u
            u=0
            v=0

            try:
                z="".join(q)
                break
            except:
                pass

            

        
        return b




        