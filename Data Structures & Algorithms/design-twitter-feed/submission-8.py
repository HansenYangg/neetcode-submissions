class Twitter:
    import heapq
    def __init__(self):
        ''' map with userId as key, then value as a sub map with:
        # { userId: {   "tweets": [...], 
                        "followers": (...),
                        "following: (...),
                        }

        instance var "counter", increments with each new tweet
        tweets array will contain tuples as elements (counter #, tweetId)

        '''
        self.counter = 0
        self.m = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # initialize mapping if user is new, else can just add to their tweets list in tuple userId: (counter #, tweetId)
        if userId in self.m:
            self.m[userId]["tweets"].append((self.counter, tweetId))
        else:
            self.m[userId] = {
                "tweets": [(self.counter, tweetId)],
                "followers": set(),
                "following": set()
            }

        self.counter += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
       # better approach (maybe still not optimal?) -- use min heap, still get all userId list of all people theyre following, and then just build the min heap with k = 10 (max size of heap) -- logn * k where k is total number of tweets we have to go through 
        if userId in self.m:
            heap = []
            following = self.m[userId]["following"] 
            following.add(userId)
            for Id in following:
                user_tweets = self.m[Id]["tweets"]

                for tweet in user_tweets:
                    heapq.heappush(heap, tweet)
                    if len(heap) > 10:
                        heapq.heappop(heap)

            following.remove(userId)
            res = []
            while heap:
                res.append(heapq.heappop(heap)[1])
            return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId -> follows followeeId (add followerId to foloweeId's followers )
        # add followeeId to followerId's following
        if followerId in self.m and followeeId in self.m:
            self.m[followeeId]["followers"].add(followerId)
            self.m[followerId]["following"].add(followeeId)

        elif followerId in self.m:
            self.m[followeeId] = {
                "tweets": [],
                "followers": set(),
                "following": set()
            }
            self.m[followeeId]["followers"].add(followerId)
            self.m[followerId]["following"].add(followeeId)

        elif followeeId in self.m:
            self.m[followerId] = {
                "tweets": [],
                "followers": set(),
                "following": set()
            }
            self.m[followeeId]["followers"].add(followerId)
            self.m[followerId]["following"].add(followeeId)

        else:
            self.m[followerId] = {
                "tweets": [],
                "followers": set(),
                "following": set()
            }
            self.m[followeeId] = {
                "tweets": [],
                "followers": set(),
                "following": set()
            }
            self.m[followeeId]["followers"].add(followerId)
            self.m[followerId]["following"].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followerId from folleeId set
        if followerId in self.m and followeeId in self.m:
            self.m[followeeId]["followers"].discard(followerId)
            self.m[followerId]["following"].discard(followeeId)

            
        
