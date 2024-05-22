class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        l=s.split()

        if len(pattern)!=len(l):
            return False
        t={}
        
        for i in range(len(pattern)):
            if pattern[i] in t.keys():
                if t[pattern[i]]!=l[i]:
                    return False
                else:
                    pass

            else:
                if l[i] in t.values():
                    return False
                else:
                    t[pattern[i]]=l[i]

        print(t)
        return True

