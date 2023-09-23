import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        s1=0
        c1=1
        while(l1):
            s1+=l1.val*c1
            c1=c1*10
            l1=l1.next

        s2=0
        c2=1
        while(l2):
            s2+=l2.val*c2
            c2=c2*10
            l2=l2.next

        prev=ListNode(None,None)
        t=prev


        
        d=str(s1+s2)
        d=d[::-1]


        for i in range(len(d)):
            g=ListNode(d[i],None)
            prev.next=g
            prev=prev.next
       # print(t.next)
        return t.next



