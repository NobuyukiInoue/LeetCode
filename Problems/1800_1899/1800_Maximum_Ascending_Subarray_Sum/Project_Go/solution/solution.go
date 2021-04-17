package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxAscendingSum(nums []int) int {
	// 0ms
	currentSum, maxSum := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i - 1] < nums[i] {
			currentSum += nums[i]
			if currentSum > maxSum {
				maxSum = currentSum
			}
		} else {
			currentSum = nums[i]
		}
	}
	return maxSum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxAscendingSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
