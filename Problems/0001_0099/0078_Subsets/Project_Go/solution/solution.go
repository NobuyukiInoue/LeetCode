package solution

import (
	"fmt"
	"strings"
	"time"
)

func subsets(nums []int) [][]int {
	// 0ms
	res := make([][]int, 0);
	res = append(res, make([]int, 0));
	for _, n := range(nums) {
		lastSize := len(res)
		for i := 0; i < lastSize; i++ {
			temp := make([]int, len(res[i]) + 1)
			copy(temp, append(res[i], n))
			res = append(res, temp)
		}
	}
	return res
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

	result := subsets(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
