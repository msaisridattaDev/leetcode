class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        c={}

        for i in nums:

            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1
        
        w=0
        
        print(c)

        for j in c.values():

            #p=j%3

            #if p%2==0:
               # w+=j/3+p/2

            if j%3==0:
                #print(j,"4")
                w+=j/3

            elif (j-2)%3==0 and j-2 >0 :
                #print(j,"1")
                w+=((j-2)/3)+1
            elif (j-4)%3==0 and j-4 >0:
                #print(j,"2")
                w+=((j-4)/3)+2

            elif j%2==0:
                #print(j,"3")
                w+=j/2

            else:
                #print(j,"5")
                return -1


        return int(w)