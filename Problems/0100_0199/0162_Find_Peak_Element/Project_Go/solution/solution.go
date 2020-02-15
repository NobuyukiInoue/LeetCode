package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findPeakElement(nums []int) int {
	// 0ms
	numsLen := len(nums)
	if numsLen == 1 || numsLen == 0 {
		return 0
	}
	if nums[0] > nums[1] {
		return 0
	}
	if nums[numsLen-1] > nums[numsLen-2] {
		return numsLen - 1
	}

	for i := 1; i < numsLen-1; i++ {
		if nums[i-1] < nums[i] && nums[i] > nums[i+1] {
			return i
		}
	}
	return 0
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + intArrayToString(nums[0]) + "]"
	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + intArrayToString(nums[i]) + "]"
	}

	return resultStr
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

	nums := str2IntArray(flds)
	fmt.Printf("nums = [%s]\n", intArrayToString(nums))

	timeStart := time.Now()

	result := findPeakElement(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
