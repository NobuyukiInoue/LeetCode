package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxDistToClosest(seats []int) int {
	n, res := len(seats), 0

	i := 0
	for j := 0; j < n; j++ {
		if seats[j] == 1 {
			if i == 0 {
				res = j
			} else {
				res = max(res, (j-i+1)/2)
			}
			i = j + 1
		}
	}

	res = max(res, n-i)
	return res
}

func max(a int, b int) int {
	if a > b {
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	seats := str2IntArray(flds)
	fmt.Printf("%s\n", printIntArray(seats))

	timeStart := time.Now()

	result := maxDistToClosest(seats)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
