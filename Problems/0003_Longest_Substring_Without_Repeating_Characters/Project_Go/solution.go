package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lengthOfLongestSubstring(s string) int {
	length := 0
	max := 0
	start := 0

	m := map[byte]int{}
	for i := 0; i < len(s); i++ {
		if index, ok := m[s[i]]; ok {
			if index < start {
				length++
			} else {
				start = index + 1
				length = i - index
			}

		} else {
			length++
		}

		m[s[i]] = i

		if length > max {
			max = length
		}
	}

	return max
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := lengthOfLongestSubstring(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %d [ms]\n\n", timeEnd.Sub(timeStart)*1000)
}
