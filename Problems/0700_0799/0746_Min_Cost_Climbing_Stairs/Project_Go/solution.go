package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minCostClimbingStairs(cost []int) int {
	mc := make([]int, len(cost)+1)
	mc[0], mc[1] = cost[0], cost[1]
	costV := 0
	for i := 2; i <= len(cost); i++ {
		if i == len(cost) {
			costV = 0
		} else {
			costV = cost[i]
		}
		mc[i] = IntMin(mc[i-1]+costV, mc[i-2]+costV)
	}

	return mc[len(cost)]
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	cost := str2IntArray(flds)
	fmt.Printf("cost = %s\n", printIntArray(cost))

	timeStart := time.Now()

	result := minCostClimbingStairs(cost)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
