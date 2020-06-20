package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func maxProduct(nums []int) int {
	// 4ms
	m := math.MinInt64
	n := m
	for _, num := range nums {
		if num >= m {
			n = m
			m = num
		} else if num > n {
			n = num
		}
	}
	return (m - 1) * (n - 1)
}

func maxProduct2(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	lenNums := len(nums)
	return ((nums[lenNums-1] - 1) * (nums[lenNums-2] - 1))
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

	result := maxProduct(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
