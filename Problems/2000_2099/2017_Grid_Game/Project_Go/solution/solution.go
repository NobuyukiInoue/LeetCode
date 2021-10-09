package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func myMax64(a int64, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func myMin64(a int64, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func mySum(nums []int) int {
	res := 0
	for _, n := range nums {
		res += n
	}
	return res
}

func gridGame(grid [][]int) int64 {
	// 144ms
	n := len(grid[0])
	top := int64(mySum(grid[0]))
	bottom, res := int64(0), int64(math.MaxInt64)
	for i := 0; i < n; i++ {
		top -= int64(grid[0][i])
		res = myMin64(res, myMax64(top, bottom))
		bottom += int64(grid[1][i])
	}
	return res
}

func gridGame1(grid [][]int) int64 {
	// 335ms
	n := len(grid[0])
	res := int64(0)
	for j := 0; j < n; j++ {
		res += int64(grid[0][j])
	}
	r2sum := int64(0)
	for j := 0; j < n; j++ {
		res = myMin64(res, myMax64(res-int64(grid[0][j]), r2sum))
		r2sum += int64(grid[1][j])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	grid := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		grid[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := gridGame(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
