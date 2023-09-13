class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        p=0
        v=""
        for i in range(len(s)):
            if i==spaces[p]:

                v+=" "
                if p <len (spaces)-1:
                    p+=1
                #v+=s[i]
            v+=s[i]
        return v
            
                

        