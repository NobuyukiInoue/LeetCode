package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func wordBreak(s string, wordDict []string) bool {
	// 0ms
	dp := make([]bool, len(s)+1)
	maxLen := 0
	for _, word := range wordDict {
		maxLen = myMax(maxLen, len(word))
	}
	for end := 1; end < len(s)+1; end++ {
		if contains(wordDict, s[:end]) {
			dp[end] = true
			continue
		}
		var i int
		if end-maxLen > 1 {
			i = end - maxLen
		} else {
			i = 1
		}
		for ; i < end; i++ {
			if dp[i] == true && contains(wordDict, s[i:end]) {
				dp[end] = true
				break
			}
		}
	}
	return dp[len(s)]
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func contains(words []string, target string) bool {
	for _, word := range words {
		if word == target {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	wordDict := strings.Split(flds[1], ",")
	fmt.Printf("s = \"%s\", wordDict = \"%s\"\n", s, wordDict)

	timeStart := time.Now()

	result := wordBreak(s, wordDict)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
