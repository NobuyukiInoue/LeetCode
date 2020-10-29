package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canPartition(nums []int) bool {
	// 12ms
	sum := 0;

	for _, n := range(nums) {
		sum += n
	}

	if (sum & 1) == 1 {
		return false
	}

	v := (sum>>1)
	dp := make([]bool, v + 1)
	dp[0] = true
	for _, n := range(nums) {
		for i := v; i >= n; i-- {
			dp[i] = dp[i] || dp[i - n]
			if(dp[v]) {
				return true
			}
		}
	}
	return dp[v]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := canPartition(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
