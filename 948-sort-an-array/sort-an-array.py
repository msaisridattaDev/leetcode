class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_both(p,q):

            p1=0
            p2=0
            t=[]
            
            while(p1<=len(p)-1 and p2<=len(q)-1 ):
                
                if p[p1]<q[p2]:
                    t.append(p[p1])
                    p1+=1
                elif q[p2]<p[p1]:
                    t.append(q[p2])
                    p2+=1
                elif q[p2]==p[p1]:
                    t.append(p[p1])
                    t.append(q[p2])
                    p2+=1
                    p1+=1
                    
            while(p1<=len(p)-1):
                t.append(p[p1])
                p1+=1
            while(p2 <=len(q)-1):
                t.append(q[p2])
                p2+=1
            
            return t
		
        def mer_arr(a,l,h):
            
            m = int((l+h)/2)
            if m==h or l==m:  
                return [a[m]]
            
            p=mer_arr(a,l,m)
            q=mer_arr(a,m,h)
            return merge_both(p,q)



        l=0
        h=len(nums)

        return mer_arr(nums,l,h)
        