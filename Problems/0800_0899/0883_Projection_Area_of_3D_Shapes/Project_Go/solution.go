package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func projectionArea(grid [][]int) int {
	res, n := 0, len(grid)
	for i, v := 0, 0; i < n; i, res, v = i+1, res+v, 0 {
		for j := 0; j < n; j++ {
			v = max(v, grid[i][j])
		}
	}
	for j, v := 0, 0; j < n; j, res, v = j+1, res+v, 0 {
		for i := 0; i < n; i++ {
			v = max(v, grid[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				res++
			}
		}
	}
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

	for i, _ := range nums {
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	grid := make([][]int, len(flds))
	fmt.Printf("grid = [")
	for i, _ := range grid {
		grid[i] = str2IntArray(flds[i])
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(grid[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(grid[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := projectionArea(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
