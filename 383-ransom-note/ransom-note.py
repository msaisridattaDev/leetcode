class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        t={}
        for i in magazine:
            if i in t.keys():
                t[i]+=1
            else:
                t[i]=1

        for j in ransomNote:
            if j in t.keys():
                if t[j]>0:
                    t[j]-=1
                    #print(j)
                else:
                    return False
            else:
                return False
        return True


        