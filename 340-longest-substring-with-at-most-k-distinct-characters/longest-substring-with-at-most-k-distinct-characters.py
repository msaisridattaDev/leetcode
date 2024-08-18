class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        j,c,ans=0,defaultdict(int),0

        for i,v in enumerate(s):

            c[v]+=1

            if len(c)<=k:
                ans+=1
            else:
                c[s[j]]-=1
                if c[s[j]]==0:
                    c.pop(s[j])
                j+=1
        
        return ans



        