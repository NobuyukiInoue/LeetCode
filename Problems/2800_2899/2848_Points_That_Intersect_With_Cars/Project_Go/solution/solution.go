package solution

import (
	"fmt"
	"strings"
	"time"
)

func numberOfPoints(nums [][]int) int {
	// 3ms - 5ms
	var lst [101]bool
	for _, cur := range nums {
		for i := cur[0]; i <= cur[1]; i++ {
			lst[i] = true
		}
	}
	ans := 0
	for i := 0; i < len(lst); i++ {
		if lst[i] {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	nums := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		nums[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(nums))

	timeStart := time.Now()

	result := numberOfPoints(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
