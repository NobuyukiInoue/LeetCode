package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func search(nums []int, target int) int {
	low, high := 0, len(nums)-1

	for low <= high {
		mid := low + ((high - low) >> 1)
		if nums[mid] == target {
			return mid
		} else if nums[mid] <= nums[high] {
			if target > nums[mid] && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		} else {
			if target >= nums[low] && target < nums[mid] {
				high = mid - 1
			} else {
				low = mid + 1
			}
		}
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

func intArray2string(arr []int) string {
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
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := str2IntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = %s\n", intArray2string(nums))
	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := search(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
