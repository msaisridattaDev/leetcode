# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        s=list1
        f=list2
        t=ListNode(0,None)
        p=t

        while(s!=None and f!=None):

            if s.val < f.val:
                t.next=s
                s=s.next
                t=t.next
            elif s.val == f.val:
                t.next=s
                s=s.next
                t=t.next
            else:
                t.next=f
                f=f.next
                t=t.next

        
        if f==None:
            t.next=s
        else:
            t.next=f

        return p.next




        