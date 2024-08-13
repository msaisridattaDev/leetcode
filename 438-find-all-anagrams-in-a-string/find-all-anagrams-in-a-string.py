import sys
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        window = len(p)
        s1_c = Counter(p)
        
        res=[]
        for i in range(len(s)-window+1):
            s2_c = Counter(s[i:i+window])
            if s2_c == s1_c:
                res.append(i)
            
        return res