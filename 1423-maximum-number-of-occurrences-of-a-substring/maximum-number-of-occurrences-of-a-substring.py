class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        m=maxLetters
        k=minSize
        count = collections.Counter(s[i:i + k] for i in range(len(s) - k + 1))
        ans=0
        
        for i,v in count.items():

            if len(set(i))>m:
                pass
            else:
                if ans<v:
                    ans=v

        return ans


