"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        m=[]
        
        if not root:
            #print(root)
            return root
       # print(root.val,root.left)
        q=[]
        q.append(root)
        c=[]
        t=[]

        while(len(q)!=0):

            #print(q)
            x=q.pop(0)
            #print(x)
            
            if x.left:
                c+=[x.left]
            
            if x.right:
                c+=[x.right]
            

            t+=[x]

            if len(q)==0:
                for i in range(len(t)):
                    #print(t)
                    if i==len(t)-1:
                        t[i].next=None
                    else:
                        #print(t[i],"once")
                        t[i].next=t[i+1]

                m+=[t]
                q=c
                c=[]
                t=[]
                #print(m)

        return root

            



        