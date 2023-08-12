package solution

import (
	"fmt"
	"strings"
	"time"
)

func lastStoneWeightII(stones []int) int {
	// 1ms
	total := 0
	for _, stone := range stones {
		total += stone
	}
	dp := make([]bool, total/2+1)
	dp[0] = true
	for _, stone := range stones {
		for j := total / 2; j >= stone; j-- {
			if dp[j-stone] {
				dp[j] = true
			}
		}
	}
	i := total / 2
	for i >= 0 && !dp[i] {
		i--
	}
	return total - 2*i
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	stones := StringToIntArray(flds)
	fmt.Printf("stones = [%s]\n", IntArrayToString(stones))

	timeStart := time.Now()

	result := lastStoneWeightII(stones)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
