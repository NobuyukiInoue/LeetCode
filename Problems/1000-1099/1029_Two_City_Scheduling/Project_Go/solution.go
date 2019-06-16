package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func twoCitySchedCost(costs [][]int) int {
	if len(costs) == 0 || len(costs[0]) == 0 {
		return 0
	}

	diff := make([]int, len(costs))
	sum := 0
	for i := 0; i < len(diff); i++ {
		sum += costs[i][0]
		diff[i] = costs[i][1] - costs[i][0]
	}

	sort.Sort(sort.IntSlice(diff))

	for i := 0; i < len(diff)/2; i++ {
		sum += diff[i]
	}

	return sum
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	costs := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		costs[i] = str2IntArray(flds[i])
	}

	fmt.Printf("costs = [")
	for i, _ := range costs {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(costs[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(costs[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := twoCitySchedCost(costs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
