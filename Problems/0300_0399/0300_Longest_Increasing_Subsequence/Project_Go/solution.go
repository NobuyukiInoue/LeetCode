package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lengthOfLIS(nums []int) int {
	tails := make([]int, len(nums))
	size := 0
	for _, x := range nums {
		i, j := 0, size
		for i != j {
			m := (i + j) / 2
			if tails[m] < x {
				i = m + 1
			} else {
				j = m
			}
		}
		tails[i] = x
		if i == size {
			size++
		}
	}
	return size
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := str2IntArray(flds)
	fmt.Printf("nums = %s\n", printIntArray(nums))

	timeStart := time.Now()

	result := lengthOfLIS(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
