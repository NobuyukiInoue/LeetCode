package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func minimumDeleteSum(s1 string, s2 string) int {
	// 4ms
	m, n := len(s1), len(s2)
	MAX := math.MaxInt64

	dp := make([][]int, m+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, n+1)
	}

	for i := m; i >= 0; i-- {
		for j := n; j >= 0; j-- {
			if i < m || j < n {
				if i < m && j < n && s1[i] == s2[j] {
					dp[i][j] = dp[i+1][j+1]
				} else {
					var t1 int
					var t2 int
					if i < m {
						t1 = (int)(s1[i]) + dp[i+1][j]
					} else {
						t1 = MAX
					}

					if j < n {
						t2 = (int)(s2[j]) + dp[i][j+1]
					} else {
						t2 = MAX
					}
					dp[i][j] = myMin(t1, t2)
				}
			}
		}
	}

	return dp[0][0]
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	s1, s2 := flds[0], flds[1]

	fmt.Printf("s1 = %s, s2 = %s\n", s1, s2)

	timeStart := time.Now()

	result := minimumDeleteSum(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
