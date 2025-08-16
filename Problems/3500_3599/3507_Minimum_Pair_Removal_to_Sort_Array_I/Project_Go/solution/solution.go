package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func minimumPairRemoval(nums []int) int {
	// 0ms
	ans := 0
	for isSorted(nums) {
		minSum, minIdx := math.MaxInt64, -1
		for i := 0; i < len(nums)-1; i++ {
			if nums[i]+nums[i+1] < minSum {
				minSum = nums[i] + nums[i+1]
				minIdx = i
			}
		}
		nums[minIdx] = minSum
		nums = removeTargetIndex(nums, minIdx+1)
		ans++
	}
	return ans
}

func isSorted(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			return true
		}
	}
	return false
}

func removeTargetIndex(nums []int, target int) []int {
	res := make([]int, len(nums)-1)
	j := 0
	for i := 0; i < len(nums); i++ {
		if i == target {
			continue
		}
		res[j] = nums[i]
		j++
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minimumPairRemoval(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
