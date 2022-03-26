package solution

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

func rangeSum(nums []int, n int, left int, right int) int {
	// 132ms - 165ms
	sums := make([]int, n*(n+1)/2)
	index := 0
	for i := 0; i < len(nums); i++ {
		current_sum := 0
		for j := i; j < len(nums); j++ {
			current_sum += nums[j]
			sums[index] = current_sum
			index++
		}
	}
	sort.Sort(sort.IntSlice(sums))
	var ans int64
	ans = 0
	for i := left - 1; i < right; i++ {
		ans += int64(sums[i])
	}
	return int(ans % int64(math.Pow(10, 9)+7))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	n, _ := strconv.Atoi(flds[1])
	left, _ := strconv.Atoi(flds[2])
	right, _ := strconv.Atoi(flds[3])
	fmt.Printf("nums = [%s], n = %d, left = %d, right = %d\n", IntArrayToString(nums), n, left, right)

	timeStart := time.Now()

	result := rangeSum(nums, n, left, right)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
