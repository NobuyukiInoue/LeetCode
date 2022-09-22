package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func answerQueries(nums []int, queries []int) []int {
	// 20ms - 31ms
	res := make([]int, len(queries))
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	for i := 0; i < len(queries); i++ {
		res[i] = sort.Search(len(nums), func(j int) bool { return nums[j] > queries[i] })
	}
	return res
}

func answerQueries2(nums []int, queries []int) []int {
	// 12ms - 25ms
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	res := make([]int, len(queries))
	for i, query := range queries {
		lo, hi := 0, len(nums)
		for lo < hi {
			mid := lo + ((hi - lo) >> 1)
			if nums[mid] <= query {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		res[i] = lo
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	queries := StringToIntArray(flds[1])
	fmt.Printf("nums = [%s], queries = [%s]\n", IntArrayToString(nums), IntArrayToString(queries))

	timeStart := time.Now()

	result := answerQueries(nums, queries)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
