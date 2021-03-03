package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestPalindromeSubseq(s string) int {
	// 12ms
	n := len(s)
	dp := make([]int, n)
	dp[n-1] = 1
	for i := n - 1; i >= 0; i-- {
		newdp := make([]int, n)
		copy(newdp, dp)
		newdp[i] = 1
		for j := i + 1; j < n; j++ {
			if s[i] == s[j] {
				newdp[j] = 2 + dp[j-1]
			} else {
				newdp[j] = myMax(dp[j], newdp[j-1])
			}
		}
		dp = newdp
	}
	return dp[n-1]
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := longestPalindromeSubseq(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
