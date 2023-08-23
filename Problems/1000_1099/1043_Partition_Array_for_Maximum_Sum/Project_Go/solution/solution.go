package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxSumAfterPartitioning(arr []int, k int) int {
	// 4ms
	n := len(arr)
	dp := make([]int, n)
	dp[0] = arr[0]
	max_val := arr[0]
	for i := 1; i < k; i++ {
		max_val = myMax(max_val, arr[i])
		dp[i] = max_val * (i + 1)
	}
	for i := k; i < n; i++ {
		max_val = arr[i]
		for j := 1; j < k+1; j++ {
			max_val = myMax(max_val, arr[i-j+1])
			dp[i] = myMax(dp[i], dp[i-j]+max_val*j)
		}
	}
	return dp[n-1]
}

func myMax(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", IntArrayToString(arr), k)

	timeStart := time.Now()

	result := maxSumAfterPartitioning(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
