class Solution:
    def removeVowels(self, s: str) -> str:
        
        p=""
        for i in s:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
                pass
            else:
                p+=i

        return p
