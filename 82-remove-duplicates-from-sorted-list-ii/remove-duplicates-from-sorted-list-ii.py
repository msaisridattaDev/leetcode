# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None:
            return None
        elif head.next==None:
            return head
        
        f=ListNode(0,None)
        q=f
        p1=head
        p2=head.next
        flag=0
        t2=p2.val
        t1=p1.val
    
        while (p2.next!=None ):

            if t1==t2:
               
                p2=p2.next
                t2=p2.val

                flag=1

            else:
                if flag==1:
                   # p2=p2.next
                    p1=p2

                    p2=p2.next
                    t2=p2.val

                   # f.next=p1
                    t1=p1.val
                    #t2=p2.val
                    flag=0

                else:
                    p1.next=p2
                    f.next=copy.deepcopy(p1)
                    f=f.next
                    #print("\n Before f is",f,"\n p1 is",p1)
                    f.next=None
                  
                    p1=p1.next
                    t1=p1.val

                    p2=p2.next
                    t2=p2.val

                #temp=p2.val
                #p2=p2.next
                #p1=p1.next
           # print(p1.val,p2.val,temp)
            
        if p1.val==p1.next.val==p2.val:
            pass
        elif p1.next.val==p2.val:
            f.next=p1
        else:
            f.next=p2

        return q.next




        

        