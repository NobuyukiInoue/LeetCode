package solution

import (
	"strconv"
	"strings"
)

func IntArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func IntIntArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return "[]"
	}

	resultStr := "[[" + IntArrayToString(nums[0]) + "]"

	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + IntArrayToString(nums[i]) + "]"
	}
	return resultStr + "]"
}

func StringToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}
