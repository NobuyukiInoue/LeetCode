package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func trap(height []int) int {
	// 0ms
	i, j := 0, len(height)-1
	left_max, right_max := 0, 0
	ans := 0
	for i < j {
		left_max = max(left_max, height[i])
		right_max = max(right_max, height[j])
		if left_max <= right_max {
			ans += left_max - height[i]
			i++
		} else {
			ans += right_max - height[j]
			j--
		}
	}
	return ans
}

func max(a int, b int) int {
	if a > b {
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
	height := strToIntArray(flds)

	fmt.Printf("height = %s\n", intArrayToString(height))
	timeStart := time.Now()

	result := trap(height)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
