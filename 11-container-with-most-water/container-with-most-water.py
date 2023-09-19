class Solution:
    def maxArea(self, height: List[int]) -> int:

        p1=0
        p2=len(height)-1
        s=0

        while(p1<p2):
            x=height[p1]
            y=height[p2]
            a=min(x,y)*(p2-p1)
            if s <a:
                s=a
            if x<y:
                p1+=1
            elif x==y:
                p1+=1
            elif x>y:
                p2-=1
            
            print(p1,p2,s)
        return s
        