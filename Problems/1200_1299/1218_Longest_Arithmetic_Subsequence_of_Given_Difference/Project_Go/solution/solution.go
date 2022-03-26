package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func longestSubsequence(arr []int, difference int) int {
	// 88ms
	dp := make(map[int]int, 0)
	ans := 0
	for _, x := range arr {
		dp[x] = dp[x-difference] + 1
		ans = myMax(ans, dp[x])
	}
	return ans
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	arr := StringToIntArray(flds[0])
	dirrerence, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], dirrerence = %d\n", IntArrayToString(arr), dirrerence)

	timeStart := time.Now()

	result := longestSubsequence(arr, dirrerence)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
