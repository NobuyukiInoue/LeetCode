package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isBoomerang(points [][]int) bool {
	return (points[0][0]-points[1][0])*(points[0][1]-points[2][1]) != (points[0][0]-points[2][0])*(points[0][1]-points[1][1])
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

	points := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		points[i] = str2IntArray(flds[i])
	}

	fmt.Printf("points = [")
	for i, _ := range points {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(points[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(points[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := isBoomerang(points)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
