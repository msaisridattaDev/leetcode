class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")

        l=[]
        for i in words:
            if len(set(i.lower()).intersection(set("asdfghjkl")))==len(set(i.lower())):
                l.append(i)
            elif len(set(i.lower()).intersection(set("qwertyuiop")))==len(set(i.lower())):
                l.append(i)
            elif len(set(i.lower()).intersection(set("zxcvbnm")))==len(set(i.lower())):
                l.append(i)

        return l