package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func orangesRotting(grid [][]int) int {
	fresh, d := 0, 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				fresh++
			}
		}
	}
	for old_fresh := fresh; fresh > 0; old_fresh = fresh {
		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[i]); j++ {
				if grid[i][j] == d+2 {
					ret := rot(&grid, i+1, j, d) + rot(&grid, i-1, j, d) + rot(&grid, i, j+1, d) + rot(&grid, i, j-1, d)
					fresh -= ret
				}
			}
		}
		if fresh == old_fresh {
			return -1
		}
		d++
	}
	return d
}

func rot(grid *[][]int, i int, j int, d int) int {
	if i < 0 || j < 0 || i >= len(*grid) || j >= len((*grid)[i]) || (*grid)[i][j] != 1 {
		return 0
	}
	(*grid)[i][j] = d + 3
	return 1
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
	for i := 0; i < len(flds); i++ {
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

	result := orangesRotting(grid)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
