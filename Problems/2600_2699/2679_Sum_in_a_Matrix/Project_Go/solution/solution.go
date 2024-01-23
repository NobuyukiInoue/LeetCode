package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func matrixSum(nums [][]int) int {
	// 105ms - 109ms
	for i, _ := range nums {
		sort.Sort(sort.IntSlice(nums[i]))
	}
	ans := 0
	for col := 0; col < len(nums[0]); col++ {
		col_max := nums[0][col]
		for i := 1; i < len(nums); i++ {
			col_max = myMax(col_max, nums[i][col])
		}
		ans += col_max
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := make([][]int, len(flds))
	for i, _ := range flds {
		nums[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("nums = %s\n", IntIntArrayToString(nums))

	timeStart := time.Now()

	result := matrixSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
