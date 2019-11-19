package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func shiftGrid(grid [][]int, k int) [][]int {
	// 32ms
	n, m := len(grid), len(grid[0])
	newGrid := make([][]int, n)
	for i := 0; i < len(newGrid); i++ {
		newGrid[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			i1 := ((i + k/m) + (j+k%m)/m) % n
			j1 := (j + k%m) % m
			newGrid[i1][j1] = grid[i][j]
		}
	}

	return newGrid
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	fld0 := strings.Split(flds[0], "],[")
	grid := make([][]int, len(fld0))
	for i := 0; i < len(grid); i++ {
		grid[i] = str2IntArray(fld0[i])
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
	fld1 := strings.Replace(flds[1], "]", "", -1)
	k, _ := strconv.Atoi(fld1)

	timeStart := time.Now()

	result := shiftGrid(grid, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
