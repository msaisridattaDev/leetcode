# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse2(self, head,right,c):

        prev=ListNode(None)
        t1=prev
        while(head!=None and c!=right):
            nxt=head.next
            head.next=prev
            prev=head
            head=nxt
            c+=1
        #print(head,prev,nxt)
        if head:
            nxt=head.next
            head.next=prev
            prev=head
        
        return [prev,nxt]





    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        t=head
        c=1
        prev=None
        if not head or head.next==None:
            return head
        

        while (head and c!=left):
            prev=head
            head=head.next
            print(t)
            c+=1

        if head and  c==left:
            p=head
            rev_list,nxt= self.reverse2(head,right,c)
            print(prev,"----",rev_list,"----",nxt,p)
        
        if prev!=None:
            prev.next=rev_list
        elif left==1:
            t=rev_list

        p.next=nxt


        return t

        
        



            



            
