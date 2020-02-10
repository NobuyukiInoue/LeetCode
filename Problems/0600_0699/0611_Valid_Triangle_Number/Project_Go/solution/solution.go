package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func triangleNumber(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	count, nums_length := 0, len(nums)
	for i := nums_length - 1; i >= 2; i-- {
		l, r := 0, i-1
		for l < r {
			if nums[l]+nums[r] > nums[i] {
				count += r - l
				r--
			} else {
				l++
			}
		}
	}

	return count
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

	result := triangleNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
