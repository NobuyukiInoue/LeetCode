package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func integerBreak(n int) int {
	// 0ms
	if n == 2 {
		return 1
	}
	if n == 3 {
		return 2
	}

	cnt2 := (3 - n%3) % 3
	cnt3 := (n - cnt2*2) / 3
	return myPow(3, cnt3) * myPow(2, cnt2)
}

func myPow(x int, n int) int {
	res := 1
	for i := n; i > 0; i-- {
		res *= x
	}
	return res
}

func integerBreak2(n int) int {
	// 0ms
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j < i; j++ {
			dp[i] = myMax(dp[i], (myMax(j, dp[j]))*(myMax(i-j, dp[i-j])))
		}
	}
	return dp[n]
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
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := integerBreak(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
