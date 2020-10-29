package solution

// 64ms

type Twitter struct {
    Watchlist map[int]map[int]struct{}
    Twitters  [][2]int
}


/** Initialize your data structure here. */
func Constructor() Twitter {
    return Twitter{
        Watchlist: make(map[int]map[int]struct{}),
        Twitters:  make([][2]int, 0),
    }
}


/** Compose a new tweet. */
func (this *Twitter) PostTweet(userId int, tweetId int)  {
    this.Twitters = append(this.Twitters, [2]int{userId, tweetId})
}


/** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
func (this *Twitter) GetNewsFeed(userId int) []int {
    twitters := []int{}
    for i := len(this.Twitters)-1; i >= 0; i-- {
        if this.Twitters[i][0] == userId {
            twitters = append(twitters, this.Twitters[i][1])
        } else {
            if _, exist := this.Watchlist[userId][this.Twitters[i][0]]; exist {
                twitters = append(twitters, this.Twitters[i][1])
            }
        }
        if len(twitters) == 10 {
            break
        }
    }
    return twitters
}


/** Follower follows a followee. If the operation is invalid, it should be a no-op. */
func (this *Twitter) Follow(followerId int, followeeId int)  {
    if this.Watchlist[followerId] == nil {
        this.Watchlist[followerId] = map[int]struct{}{}
    }
    this.Watchlist[followerId][followeeId] = struct{}{}
}


/** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
func (this *Twitter) Unfollow(followerId int, followeeId int)  {
    if this.Watchlist[followerId] == nil {
        return
    }
    delete(this.Watchlist[followerId], followeeId)
}

/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */
