package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxLength(arr []string) int {
	// 0ms
	dp := []int{0}
	res := 0
	for _, st := range arr {
		a, dup := 0, 0
		for _, ch := range st {
			dup |= a & (1 << ((uint)(ch) - 'a'))
			a |= 1 << ((uint)(ch) - 'a')
		}
		if dup > 0 {
			continue
		}
		for i := len(dp) - 1; i >= 0; i-- {
			if (dp[i] & a) > 0 {
				continue
			}
			dp = append(dp, dp[i]|a)
			res = myMax(res, bitCount(dp[i]|a))
		}
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func bitCount(a int) int {
	count := 0
	for ; a > 0; a >>= 1 {
		if a%2 == 1 {
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)

	arr := strings.Split(temp, ",")
	fmt.Printf("arr = %s\n", arr)

	timeStart := time.Now()

	result := maxLength(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
