package solution

import (
	"fmt"
	"strings"
	"time"
)

func permute(nums []int) [][]int {
	// 0ms
	result := make([][]int, 0)
	helper(nums, []int{}, &result)
	return result
}

func helper(nums []int, subres []int, result *[][]int) {
	if len(nums) == 0 {
		*result = append(*result, subres)
		return
	}

	for i, num := range nums {
		numsCopy := append([]int{}, nums...)
		subresCopy := append([]int{}, subres...)
		helper(append(numsCopy[:i], numsCopy[i+1:]...), append(subresCopy, num), result)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	timeStart := time.Now()

	result := permute(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
