package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numMagicSquaresInside(grid [][]int) int {
	cnt := 0
	for i := 0; i <= len(grid)-3; i++ {
		for j := 0; j <= len(grid[0])-3; j++ {
			if helper(i, j, grid) {
				cnt++
			}
		}
	}
	return cnt
}

func helper(x int, y int, grid [][]int) bool {
	if grid[x+1][y+1] != 5 {
		return false
	}

	valid := make([]int, 16)

	for i := x; i <= x+2; i++ {
		for j := y; j <= y+2; j++ {
			valid[grid[i][j]]++
		}
	}

	for v := 1; v <= 9; v++ {
		if valid[v] != 1 {
			return false
		}
	}

	if grid[x][y]+grid[x][y+1]+grid[x][y+2] != 15 {
		return false
	}
	if grid[x][y]+grid[x+1][y+1]+grid[x+2][y+2] != 15 {
		return false
	}
	if grid[x][y]+grid[x+1][y]+grid[x+2][y] != 15 {
		return false
	}
	if grid[x+2][y]+grid[x+2][y+1]+grid[x+2][y+2] != 15 {
		return false
	}
	if grid[x][y+2]+grid[x+1][y+2]+grid[x+2][y+2] != 15 {
		return false
	}
	if grid[x][y+2]+grid[x+1][y+1]+grid[x+2][y] != 15 {
		return false
	}

	return true
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
		fmt.Printf("%s\n", printIntArray(grid[i]))
	}

	timeStart := time.Now()

	result := numMagicSquaresInside(grid)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
