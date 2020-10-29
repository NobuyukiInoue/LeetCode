package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execTwitter(cmds []string, args [][]int) {
	obj := Constructor()
	createdTwitter := false

	for i, cmd := range cmds {
		if cmd == "Twitter" {
			createdTwitter = true

		} else {
			if createdTwitter != true {
				fmt.Printf("Twitter was not created.\n")
				os.Exit(1)
			}

			if cmd == "postTweet" {
				obj.PostTweet(args[i][0], args[i][1])
				fmt.Printf("PostTweet(%d, %d)\n", args[i][0], args[i][1])

			} else if cmd == "getNewsFeed" {
				result := obj.GetNewsFeed(args[i][0])
				fmt.Printf("GetNewsFeed() ... %s\n",  IntArrayToString(result))

			} else if cmd == "follow" {
				obj.Follow(args[i][0], args[i][1])
				fmt.Printf("follow(%d, %d)\n", args[i][0], args[i][1])

			} else if cmd == "unfollow" {
				obj.Unfollow(args[i][0], args[i][1])
				fmt.Printf("unfollow(%d, %d)\n", args[i][0], args[i][1])

			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)

	flds := strings.Split(temp, "],[[")

	flds[0] = strings.Replace(flds[0], "[[", "", -1)
	cmds := strings.Split(flds[0], ",")

	flds[1] = strings.Replace(flds[1], "]]]", "", -1)
	argsStr := strings.Split(flds[1], "],[")

	vals := make([][]int, len(argsStr))
	for i, _ := range(argsStr) {
		if argsStr[i] == "" {
		
		} else {
		    flds2 := strings.Split(argsStr[i], ",")
			vals[i] = make([]int, len(flds2))
			for j, _ := range(flds2) {
			    vals[i][j], _ = strconv.Atoi(flds2[j])
			}
		}
	}

	fmt.Printf("cmds[] = [%s]\n", StringArrayToString(cmds))
	fmt.Printf("vals[] = [%s]\n", IntIntArrayToString(vals))

	timeStart := time.Now()

	execTwitter(cmds, vals)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
