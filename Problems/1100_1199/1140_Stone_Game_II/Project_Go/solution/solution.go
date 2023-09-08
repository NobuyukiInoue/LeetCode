package solution

import (
	"fmt"
	"strings"
	"time"
)

func stoneGameII(piles []int) int {
	// 0ms
	if len(piles) == 0 {
		return 0
	}
	dp := make([][]int, len(piles))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, len(piles))
	}
	suffixSum := make([]int, len(piles))
	suffixSum[len(suffixSum)-1] = piles[len(piles)-1]
	for i := len(piles) - 2; i >= 0; i-- {
		suffixSum[i] = piles[i] + suffixSum[i+1]
	}
	return helper(piles, dp, suffixSum, 0, 1)
}

func helper(piles []int, dp [][]int, suffixSum []int, i int, M int) int {
	if i == len(piles) {
		return 0
	}
	if i+2*M >= len(piles) {
		return suffixSum[i]
	}
	if dp[i][M] != 0 {
		return dp[i][M]
	}
	result := 0
	for x := 1; x <= 2*M; x++ {
		result = myMax(result, suffixSum[i]-helper(piles, dp, suffixSum, i+x, myMax(M, x)))
	}
	dp[i][M] = result
	return result
}

func myMax(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	piles := StringToIntArray(flds)
	fmt.Printf("piles = [%s]\n", IntArrayToString(piles))

	timeStart := time.Now()

	result := stoneGameII(piles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
