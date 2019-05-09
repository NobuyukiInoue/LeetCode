package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func search(nums []int, target int) int {
	ans := -1
	lo, hi := 0, len(nums)

	for lo < hi {
		mid := lo + (hi-lo)/2

		if nums[mid] == target {
			ans = mid
			break
		}

		if nums[mid] < target {
			lo = mid + 1
		}

		if nums[mid] > target {
			hi = mid
		}
	}

	return ans
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := str2IntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = %s, target = %d\n", printIntArray(nums), target)

	timeStart := time.Now()

	result := search(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
