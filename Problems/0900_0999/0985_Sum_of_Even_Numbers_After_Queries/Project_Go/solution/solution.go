package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	// 60ms
	even_sum := 0
	for _, num := range nums {
		if num%2 == 0 {
			even_sum += num
		}
	}
	ans := make([]int, len(queries))
	for i, query := range queries {
		val, index := query[0], query[1]
		even_sum -= (((nums[index] + 1) & 1) * nums[index])
		nums[index] = (nums[index] + val)
		even_sum += (((nums[index] + 1) & 1) * nums[index])
		ans[i] = even_sum
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	flds := strings.Split(temp, "],[[")

	nums := StringToIntArray(strings.Replace(flds[0], "[", "", -1))

	flds1 := strings.Split(flds[1], "],[")
	var queries [][]int
	if len(flds1) == 0 {
		queries = make([][]int, 0)
	} else {
		queries = make([][]int, len(flds1))
		for i := 0; i < len(flds1); i++ {
			queries[i] = StringToIntArray(flds1[i])
		}
	}
	fmt.Printf("nums = [%s], queries = %s\n", IntArrayToString(nums), IntIntArrayToString(queries))

	timeStart := time.Now()

	result := sumEvenAfterQueries(nums, queries)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
