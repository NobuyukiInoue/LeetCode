package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numRollsToTarget(d int, f int, target int) int {
	// 0ms
	if f*d < target {
		return 0
	}
	if d == 1 {
		return 1
	}

	dp := make([][]int, d+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, target+1)
	}

	for i := 1; i <= f && i <= target; i++ {
		dp[1][i] = 1
	}

	for k := 2; k <= d; k++ {
		for i := 1; i <= f && i <= target; i++ {
			for j := 1; j <= target-i; j++ {
				if j+i <= target {
					dp[k][j+i] = (dp[k][j+i] + dp[k-1][j]) % (1000000007)
				}
			}
		}
	}

	return dp[d][target]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	d, _ := strconv.Atoi(flds[0])
	f, _ := strconv.Atoi(flds[1])
	target, _ := strconv.Atoi(flds[2])
	fmt.Printf("d = %d, f = %d, target = %d\n", d, f, target)

	timeStart := time.Now()

	result := numRollsToTarget(d, f, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
