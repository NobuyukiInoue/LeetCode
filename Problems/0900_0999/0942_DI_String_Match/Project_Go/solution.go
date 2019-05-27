package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func diStringMatch(S string) []int {
	n := len(S)
	left, right := 0, n
	res := make([]int, n+1)

	for i := 0; i < n; i++ {
		if S[i] == 'I' {
			res[i] = left
			left++
		} else {
			res[i] = right
			right--
		}
	}
	res[n] = left
	return res
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
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := diStringMatch(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
