package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getMaximumGold(grid [][]int) int {
	// 16ms
	max := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] != 0 {
				count := helper(grid, i, j, 0)
				if count > max {
					max = count
				}
			}
		}
	}
	return max
}

func helper(grid [][]int, i int, j int, count int) int {
	if grid[i][j] == 0 {
		return count
	}
	count += grid[i][j]
	temp := grid[i][j]
	grid[i][j] = 0
	sums := []int{0, 0, 0, 0}
	if i > 0 {
		sums[0] = helper(grid, i-1, j, count)
	}
	if i < len(grid)-1 {
		sums[1] = helper(grid, i+1, j, count)
	}
	if j > 0 {
		sums[2] = helper(grid, i, j-1, count)
	}
	if j < len(grid[i])-1 {
		sums[3] = helper(grid, i, j+1, count)
	}
	grid[i][j] = temp
	return myMax(sums)
}

func myMax(data []int) int {
	max := data[0]
	for i := 1; i < len(data); i++ {
		if data[i] > max {
			max = data[i]
		}
	}
	return max
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

	result := getMaximumGold(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
