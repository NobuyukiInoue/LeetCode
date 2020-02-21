package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countNegatives(grid [][]int) int {
	// 12ms
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] < 0 {
				count++
			}
		}
	}
	return count
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func printGrid(title string, grid [][]int) {
	fmt.Printf("%s = [", title)
	for i, _ := range grid {
		if i == 0 {
			fmt.Printf(" [%s]", intArrayToString(grid[i]))
		} else {
			fmt.Printf(",[%s]", intArrayToString(grid[i]))
		}
	}
	fmt.Printf("]\n")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)
	nums := strings.Split(flds, "],[")

	grid := make([][]int, len(nums))
	for i := 0; i < len(nums); i++ {
		grid[i] = strToIntArray(nums[i])
	}
	printGrid("grid", grid)

	timeStart := time.Now()

	result := countNegatives(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
