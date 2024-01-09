class Solution:
    def reformatDate(self, date: str) -> str:
        
        c={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        e=date.split()

        if len(e[0])==3:
            e[0]="0"+e[0]

        e=e[::-1]
        ans=""

        for j,v in enumerate(e):

            if j==len(e)-1:
                ans+=v[:2]

            elif v in c.keys():
                ans+=c[v]
            
            else:
                ans+=v
            
            ans+="-"

        return ans[:-1]


