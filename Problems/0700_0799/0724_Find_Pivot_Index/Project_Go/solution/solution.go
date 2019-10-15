package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func pivotIndex(nums []int) int {
	if len(nums) <= 2 {
		return -1
	}

	s, leftSum := 0, 0
	for _, x := range nums {
		s += x
	}

	for i, value := range nums {
		if leftSum*2+value == s {
			return i
		}
		leftSum += value
	}

	return -1
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := str2IntArray(flds)

	fmt.Printf("nums = %s\n", printIntArray(nums))

	timeStart := time.Now()

	result := pivotIndex(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
