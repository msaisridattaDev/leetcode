class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        c={}

        q=[0]
        c[0]=1

        while q:

            p=q.pop(0)

            for i in rooms[p]:

                if i not in c.keys():
                    c[i]=1
                    q.append(i)

        for v in range(n):
            if v not in c.keys():
                return False
        
        return True




        
