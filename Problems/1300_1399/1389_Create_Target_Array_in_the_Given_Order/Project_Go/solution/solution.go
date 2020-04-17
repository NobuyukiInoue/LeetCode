package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func createTargetArray(nums []int, index []int) []int {
	// 0ms
	targetArray := make([]int, len(nums))
	for i, idx := range index {
		copy(targetArray[idx+1:i+1], targetArray[idx:i])
		targetArray[idx] = nums[i]
	}
	return targetArray
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
		return "[]"
	}

	resultStr := "[" + strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := strToIntArray(flds[0])
	index := strToIntArray(flds[1])
	fmt.Printf("nums = %s, index = %s\n", intArrayToString(nums), intArrayToString(index))

	timeStart := time.Now()

	result := createTargetArray(nums, index)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
