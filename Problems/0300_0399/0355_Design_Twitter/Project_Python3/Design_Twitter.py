import collections
import heapq
import itertools
import os
import sys
import time

class Twitter:
    # 80ms

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))


#   def getNewsFeed(self, userId: int) -> List[int]:
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Solution:
    def execTwitter(self, cmds, args):
        for i in range(len(cmds)):
            if cmds[i] == "Twitter":
                twitter = Twitter()
                print("Execute Twitter()")
            else:
                if twitter is None:
                    print("twitter not found... {0}".format(cmds[i]))
                    exit(1)

                elif cmds[i] == "postTweet":
                    twitter.postTweet(args[i][0], args[i][1])
                    print("postTweet({0:d}, {1:d})".format(args[i][0], args[i][1]))

                elif cmds[i] == "getNewsFeed":
                    result = twitter.getNewsFeed(args[i])
                    print("getNewsFeed({0:d}) ==> {1}".format(args[i], result))

                elif cmds[i] == "follow":
                    result = twitter.follow(args[i][0], args[i][1])
                    print("follow({0:d}, {1:d})".format(args[i][0], args[i][1]))

                elif cmds[i] == "unfollow":
                    result = twitter.unfollow(args[i][0], args[i][1])
                    print("unfollow({0:d}, {1:d})".format(args[i][0], args[i][1]))

                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")
    cmds = flds[0].replace("[[","").split(",")
    args_str = flds[1].replace("]]]", "").split("],[")
    print(args_str)

    args = [None]*len(args_str)
    for i, _ in enumerate(args_str):
        if args_str[i] == "":
            args[i] = None
        elif "," in args_str[i]:
            args[i] = [int(n) for n in args_str[i].split(",")]
        else:
            args[i] = int(args_str[i])

    print("cmds[] = {0}",format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()

    result = sl.execTwitter(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
