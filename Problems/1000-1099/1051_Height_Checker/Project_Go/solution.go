package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func heightChecker(heights []int) int {
	sorted := make([]int, len(heights))
	copy(sorted[:], heights)
	sort.Ints(sorted)

	count := 0
	for i, _ := range heights {
		if sorted[i] != heights[i] {
			count++
		}
	}

	return count
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

	heights := str2IntArray(flds)
	fmt.Printf("heights = %s\n", printIntArray(heights))

	timeStart := time.Now()

	result := heightChecker(heights)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
