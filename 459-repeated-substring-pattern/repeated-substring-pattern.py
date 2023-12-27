class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        p=""
        for i in s:
            p+=i

            u=len(s)-len(p)

            if (int(u/len(p))+1)*p ==s and len(p)!=len(s):
                    return True
        
        return False


        