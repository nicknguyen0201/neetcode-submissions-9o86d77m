from heapq import heappush, heappop
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.postMap=defaultdict(list)#user id -> post of 10 most recent post list
        self.following=defaultdict(set) # user id ->set()#people I am following 
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        posts=self.postMap[userId]
        while len(posts)>=10:
            posts.pop(0)
        posts.append((self.time, tweetId))
        self.time+=1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        recent_heap =[]
        following = self.following[userId]#set of ppl I follow
        #add mysef
        following.add(userId)
        if len(following)>10: #if I am following 1000 people
            #build a heap to keep track of the most recent 10
            for followeeId in following:
                end = len(self.postMap[followeeId])-1
                if end>=0:
                    most_recent_post=self.postMap[followeeId][end][1]
                    t = self.postMap[followeeId][end][0]
                    heappush(recent_heap,
                    (t, most_recent_post,followeeId, end-1)
                    )
                if len(recent_heap)>10:
                    heappop(recent_heap)

        else:
            for followeeId in following:
                end = len(self.postMap[followeeId])-1
                if end>=0:
                    most_recent_post=self.postMap[followeeId][end][1]
                    t = self.postMap[followeeId][end][0]
                    heappush(recent_heap,
                    (t, most_recent_post,followeeId, end-1)
                    ) 
        #now we hace a recent heap contain <=10 post 
        #but requirement say the heap need to be return in most recent time
        #and 1 user I follow could have made a lot of new post recently, more recent than anyone else
        
        min_heap=[]
        while recent_heap:
            t,post_id, f_id, idx = heappop(recent_heap)
            heappush (min_heap, (-t,post_id, f_id, idx))#keep track of most recent time 
        #merge k sorted list
        res=[]
        while len(res)<10 and min_heap:
            t,post_id, f_id, idx = heappop(min_heap)
            res.append(post_id)
            if idx>=0:
                prev_post = self.postMap[f_id][idx][1]
                time=self.postMap[f_id][idx][0]
                
                heappush(min_heap, (-time,prev_post, f_id, idx-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
