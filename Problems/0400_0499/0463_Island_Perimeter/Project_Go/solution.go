package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func islandPerimeter(grid [][]int) int {
	island, redge := 0, 0
	row, col := len(grid), len(grid[0])
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 1 {
				island++
				if j < col-1 && grid[i][j+1] == 1 {
					redge++
				}
				if i < row-1 && grid[i+1][j] == 1 {
					redge++
				}
			}
		}
	}

	return 4*island - 2*redge
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

	result := islandPerimeter(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
