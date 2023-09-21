# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        prev=ListNode(None,None)
        t1=prev
        nxt=ListNode(None,None)
        t2=nxt
        while(head):
            if head.val < x:
                prev.next=copy.deepcopy(head)
                prev=prev.next
                prev.next=None
                head=head.next
                #print(head,"\n\n prev is",prev,"\n\n nxt is",nxt)
            else:
                nxt.next=copy.deepcopy(head)
                nxt=nxt.next
                nxt.next=None
                head=head.next
                #print(head,"\n\n prev is",prev,"\n\n nxt is",nxt)
            
           # print(head,"\n\n prev is",prev,"\n\n nxt is",nxt)

        prev.next=t2.next

        return t1.next



        
        