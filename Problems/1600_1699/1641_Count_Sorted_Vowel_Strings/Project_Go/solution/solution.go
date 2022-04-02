package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countVowelStrings(n int) int {
	// 0ms
	var dp [5]int
	for i := 0; i < len(dp); i++ {
		dp[i] = 1
	}
	for i := 2; i < n+1; i++ {
		for j := 1; j < 5; j++ {
			dp[j] = dp[j] + dp[j-1]
		}
	}
	ans := 0
	for i := 0; i < len(dp); i++ {
		ans += dp[i]
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := countVowelStrings(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
