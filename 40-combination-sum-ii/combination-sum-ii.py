class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        candidates.sort()
        l=[]
        t={}
        def combinationSum3(candidates,i,l,sum1,t):

    

            if sum1==target:
                
                if tuple(l) not in t.keys():
                    t[tuple(l)]=1
                return

            if i>=len(candidates):
                return

            if sum1> target:
                return
            
                
            combinationSum3(candidates,i+1,l+[candidates[i]],sum1+candidates[i],t)
        
            while len(candidates)-1 >=i+1>=0 and candidates[i]==candidates[i+1]:
                i+=1
            
            combinationSum3(candidates,i+1,l,sum1,t)

        

        combinationSum3(candidates,0,l,0,t)

        return t



        