package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func permute(nums []int) [][]int {
	// 0ms
	result := make([][]int, 0)
	helper(nums, []int{}, &result)
	return result
}

func helper(nums []int, subres []int, result *[][]int) {
	if len(nums) == 0 {
		*result = append(*result, subres)
		return
	}

	for i, num := range nums {
		numsCopy := append([]int{}, nums...)
		subresCopy := append([]int{}, subres...)
		helper(append(numsCopy[:i], numsCopy[i+1:]...), append(subresCopy, num), result)
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

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}
	resultStr := "[" + intArrayToString(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + intArrayToString(nums[i])
	}

	return resultStr + "]"
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := strToIntArray(flds)

	fmt.Printf("nums = %s\n", intArrayToString(nums))
	timeStart := time.Now()

	result := permute(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intintArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
