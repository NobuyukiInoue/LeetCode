package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxProduct(nums []int) int {
	// 0ms
	if nums == nil || len(nums) == 0 {
		return 0
	}
	maxP := make([]int, len(nums))
	minP := make([]int, len(nums))
	maxP[0], minP[0] = nums[0], nums[0]
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		maxP[i] = Max(Max(maxP[i-1]*nums[i], minP[i-1]*nums[i]), nums[i])
		minP[i] = Min(Min(maxP[i-1]*nums[i], minP[i-1]*nums[i]), nums[i])
		res = Max(res, maxP[i])
	}
	return res
}

func Max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func Min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
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

	result := maxProduct(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
