class Solution:
    def sortSentence(self, s: str) -> str:

        x=s.split()

        for u in range(len(x)):

            x[u]=x[u][-1]+x[u][0:len(x[u])-1]

        x.sort()

        for v in range(len(x)):

            x[v]=x[v][1::]

        

        return " ".join(x)

        



        