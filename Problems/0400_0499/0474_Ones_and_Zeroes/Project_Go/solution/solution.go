package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findMaxForm(strs []string, m int, n int) int {
	// 24ms
	dp := make([][]int, m+1)
	for i, _ := range dp {
		dp[i] = make([]int, n+1)
	}
	for _, curr := range strs {
		zeroCount := getCount(curr)
		oneCount := len(curr) - zeroCount
		for i := m; i >= zeroCount; i-- {
			for j := n; j >= oneCount; j-- {
				dp[i][j] = myMax(dp[i][j], 1+dp[i-zeroCount][j-oneCount])
			}
		}
	}
	return dp[m][n]
}

func getCount(curr string) int {
	res := 0
	for i, _ := range curr {
		if curr[i] == '0' {
			res++
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	strs := strings.Split(flds[0], ",")
	m, _ := strconv.Atoi(flds[1])
	n, _ := strconv.Atoi(flds[2])
	fmt.Printf("strs = [%s], m = %d, n = %d\n", StringArrayToString(strs), m, n)

	timeStart := time.Now()

	result := findMaxForm(strs, m, n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
