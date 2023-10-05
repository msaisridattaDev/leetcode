class Solution:
    def intToRoman(self, num: int) -> str:
        h={1:"I", 5:"V" , 10:"X" , 50:"L" , 100:"C" , 500:"D",1000:"M" }
        t={0:[1,5],1:[10,50],2:[100,500],3:[1000]}
        nums=str(num)
        p_zeros=len(nums)-1
        res=""

        for i in nums:
        
            p_value= int(i)*10**(p_zeros)
            
            if int(i)!=4 and int(i)!=9 and int(i)!=0:
                for j in t[p_zeros]:
                    #print(j,p_value)
                    if p_value >=j:
                        q=j
                        r_value=p_value-q

                r_str=int(str(r_value)[0])
                print(p_value,q,h[q],h[t[p_zeros][0]]*r_str)
                res+=h[q]+h[t[p_zeros][0]]*r_str

            elif int(i)==4:

                res+=h[t[p_zeros][0]]+h[t[p_zeros][1]]

            elif int(i)==9:

                res+=h[t[p_zeros][0]]+h[t[p_zeros+1][0]]
            
            p_zeros-=1

      



        return res



        