class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        t=[]
        q={}

        if len(s)!=len(goal):
            return False
        if s==goal:
            if len(set(s))!=len(s):
                return True
        
        for i in range(len(s)):

            if s[i]==goal[i]:
                continue
            else:
                t+=[i]

        if len(t)==2:

            x,y=t
            print(x,y)
            if s[y]+s[x]==goal[x]+goal[y]:
                return True

        
        return False

        