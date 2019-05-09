package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lemonadeChange(bills []int) bool {
	five, ten := 0, 0
	for _, value := range bills {
		if value == 5 {
			five++
		} else if value == 10 {
			five--
			ten++
		} else if ten > 0 {
			ten--
			five--
		} else {
			five -= 3
		}
		if five < 0 {
			return false
		}
	}
	return true
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

	bills := str2IntArray(flds)
	fmt.Printf("bills = %s\n", printIntArray(bills))

	timeStart := time.Now()

	result := lemonadeChange(bills)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
