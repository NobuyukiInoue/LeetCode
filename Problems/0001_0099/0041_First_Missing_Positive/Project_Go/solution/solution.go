package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func firstMissingPositive(nums []int) int {
	// 0ms
	start := 0
	end := len(nums) - 1
	for start <= end {
		index := nums[start] - 1
		if index == start {
			start++
		} else if index < 0 || index > end || nums[start] == nums[index] {
			nums[start] = nums[end]
			end--
		} else {
			nums[start] = nums[index]
			nums[index] = index + 1
		}
	}
	return start + 1
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := strToIntArray(flds)

	fmt.Printf("nums = %s\n", intArrayToString(nums))
	timeStart := time.Now()

	result := firstMissingPositive(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
