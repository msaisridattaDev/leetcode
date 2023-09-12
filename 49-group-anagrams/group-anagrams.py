class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m={}
        for i in strs:
            t={}
            for j in i:
                if j in t.keys():
                    t[j]+=1
                else:
                    t[j]=1

            p=str(sorted(t.items()))

            if p in m.keys():
                m[p]+=[i]
            else:
                m[p]=[i]

        return list(m.values())
        