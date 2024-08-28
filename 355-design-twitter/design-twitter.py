from heapq import _heapify_max , _heappop_max

class Twitter:

    def __init__(self):
        self.ctsmp=0
        self.l={}
        self.users={}
        self.user_tstmps={}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users.keys():
            self.users[userId]=[]
        
        self.ctsmp+=1
        self.l[self.ctsmp]=tweetId


        if userId not in self.user_tstmps.keys():
            self.user_tstmps[userId]=[self.ctsmp]
        else:
            self.user_tstmps[userId]+=[self.ctsmp]

        


    def getNewsFeed(self, userId: int) -> List[int]:

        ans=[]
        if userId in self.users.keys():
            y=[userId]
            y.extend(self.users[userId])

            t=[]
            
           # print(self.l,y,t,self.user_tstmps)
            for i in y:
                if i in self.user_tstmps.keys():
                    t.extend(self.user_tstmps[i][-1:-11:-1])
            
            print(t,y,self.user_tstmps)
            _heapify_max(t)
            g=10
            #print(self.l,y,t)
            while(len(t)!=0 and g>0):
        
                ans.append( self.l[_heappop_max(t)])
                g-=1

        return ans


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users.keys() :
            self.users[followerId]=[]

        if followeeId not in self.users.keys() :
            self.users[followeeId]=[]

        if followeeId not in self.users[followerId]:
            self.users[followerId]+=[followeeId]


    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)