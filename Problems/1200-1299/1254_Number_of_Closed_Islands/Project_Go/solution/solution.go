package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func closedIsland(grid [][]int) int {
	// 8ms
	if grid == nil || len(grid[0]) == 0 {
		return 0
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if i == 0 || j == 0 || i == len(grid)-1 || j == len(grid[i])-1 && grid[i][j] == 0 {
				dfs(grid, i, j, 1)
			}
		}
	}

	res := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 0 {
				dfs(grid, i, j, 1)
				res++
			}
		}
	}

	return res
}

func dfs(grid [][]int, i int, j int, val int) {
	if 0 <= i && i < len(grid) && 0 <= j && j < len(grid[0]) && grid[i][j] == 0 {
		grid[i][j] = val
		dfs(grid, i, j+1, val)
		dfs(grid, i+1, j, val)
		dfs(grid, i-1, j, val)
		dfs(grid, i, j-1, val)
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]int, len(flds))
	for i := 0; i < len(grid); i++ {
		grid[i] = str2IntArray(flds[i])
	}

	fmt.Printf("grid = [")
	for i, _ := range grid {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(grid[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(grid[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := closedIsland(grid)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
