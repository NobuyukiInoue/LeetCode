package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxWidthRamp(A []int) int {
	// 36ms
	size := len(A)

	stack := make([]int, 1, size)
	top := 0
	for i := 1; i < size; i++ {
		if A[stack[top]] > A[i] {
			stack = append(stack, i)
			top++
		}
	}

	res := 0
	for j := size - 1; j >= 0 && top >= 0; j-- {
		width := 0
		for top >= 0 && A[stack[top]] <= A[j] {
			width = j - stack[top]
			stack = stack[:top]
			top--
		}
		res = max(res, width)
	}

	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
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

	A := str2IntArray(flds)

	fmt.Printf("A = %s\n", printIntArray(A))

	timeStart := time.Now()

	result := maxWidthRamp(A)

	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
