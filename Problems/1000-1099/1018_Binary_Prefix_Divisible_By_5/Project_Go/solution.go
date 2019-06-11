package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func prefixesDivBy5(A []int) []bool {
	total := 0
	lenA := len(A)
	result := make([]bool, lenA)
	for i := 0; i < lenA; i++ {
		//total = (total*2 + A[i]) % 5
		total = ((total << 1) + A[i]) % 5
		if total == 0 {
			result[i] = true
		} else {
			result[i] = false
		}
	}
	return result
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

func printBoolArray(nums []bool) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatBool(nums[i])
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

	result := prefixesDivBy5(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printBoolArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
