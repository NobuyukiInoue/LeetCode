package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func new21Game(N int, K int, W int) float64 {
	// 0ms
	if K == 0 || N >= K+W {
		return 1
	}
	dp := make([]float64, N+1)
	Wsum, res := float64(1), float64(0)
	dp[0] = 1
	for i := 1; i <= N; i++ {
		dp[i] = Wsum / float64(W)
		if i < K {
			Wsum += dp[i]
		} else {
			res += dp[i]
		}
		if i-W >= 0 {
			Wsum -= dp[i-W]
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	N, _ := strconv.Atoi(flds[0])
	K, _ := strconv.Atoi(flds[1])
	W, _ := strconv.Atoi(flds[2])
	fmt.Printf("N, K, W = %d, %d, %d\n", N, K, W)

	timeStart := time.Now()

	result := new21Game(N, K, W)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
