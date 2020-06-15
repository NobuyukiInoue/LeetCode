package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func runningSum(nums []int) []int {
	// 4ms
	numsLen := len(nums)
	res := make([]int, numsLen)
	res[0] = nums[0]
	for i := 1; i < numsLen; i++ {
		res[i] = res[i-1] + nums[i]
	}
	return res
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
	fmt.Printf("nums = [%s]\n", intArrayToString(nums))

	timeStart := time.Now()

	result := runningSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
