package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findLengthOfLCIS(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}
	count, max_count := 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			count++
			if count > max_count {
				max_count = count
			}
		} else {
			count = 1
		}
	}

	return max_count
}

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	nums := make([]int, len(flds))
	for i, _ := range flds {
		nums[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("nums = %s\n", IntArray2string(nums))

	timeStart := time.Now()

	result := findLengthOfLCIS(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
