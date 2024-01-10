class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums=temperatures
        d=len(nums)-1
        
        t=[0]
        l=[[nums[-1],d]]


        for i in range((len(nums))-2,-1,-1):

            p,q=l.pop()

           # print(nums[i],p,q)

            if nums[i]>p:
    
                while (nums[i]>=p):
                    
                    if len(l)>0:
                        p,q=l.pop()

                        #print("popped",p,q)
                    else:
                        flag=True
                        break
                
                if not flag:
                    l.append([p,q])
                    l.append([nums[i],i])
                    print(q,i)
                    t.append(abs(q-i))
                else:
                    l=[[nums[i],i]]
                    t.append(0)

            elif nums[i]==p:
                if len(l)>0:
                    t.append(l[-1][1]-i)
                else:
                    #print(q,i,l)
                    #t.append(abs(q-i))
                    t.append(0)
                l.append([nums[i],i])
                
                
                

            else:
                l.append([p,q])
                l.append([nums[i],i])
                t.append(abs(q-i))

                
            if len(l)==0:
                l=[[nums[i],i]]
                t.append(0)
            
            flag=False
            #print("after",l)
                
        #print(t)
           

        
        return t[::-1] 