class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        x=[]
        y=[]
        
        for i in moves:
            if i=="_":
                x.append("R")
                y.append("L")
            else:
                x.append(i)
                y.append(i)

        z=0
        for j in x:
            if j=="L":
                z-=1
            else:
                z+=1

        p=0

        for h in y:
            if h=="L":
                p-=1
            else:
                p+=1

        return(max(abs(z),abs(p)))


        





        return 10


            