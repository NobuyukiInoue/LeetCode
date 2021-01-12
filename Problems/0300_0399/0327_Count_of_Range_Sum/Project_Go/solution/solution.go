package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countRangeSum(nums []int, lower int, upper int) int {
	// 16ms
	n := len(nums)
	sum := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		sum[i] = sum[i-1] + int64(nums[i-1])
	}
	return merge(sum, 0, n, lower, upper)
}

func merge(sum []int64, l, r, lower, upper int) int {
	if l >= r {
		return 0
	}
	mid := (l + r) / 2
	count := 0
	count += merge(sum, l, mid, lower, upper) + merge(sum, mid+1, r, lower, upper)
	m, n := mid+1, mid+1
	for i := l; i <= mid; i++ {
		for m <= r && sum[m]-sum[i] < int64(lower) {
			m++
		}
		for n <= r && sum[n]-sum[i] <= int64(upper) {
			n++
		}
		count += n - m
	}
	left := append([]int64{}, sum[l:mid+1]...)
	right := append([]int64{}, sum[mid+1:r+1]...)
	i := l
	ll := 0
	rr := 0
	for ll < len(left) && rr < len(right) {
		if left[ll] < right[rr] {
			sum[i] = left[ll]
			ll++
		} else {
			sum[i] = right[rr]
			rr++
		}
		i++
	}
	for rr < len(right) {
		sum[i] = right[rr]
		rr++
		i++
	}
	for ll < len(left) {
		sum[i] = left[ll]
		ll++
		i++
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	lower, _ := strconv.Atoi(flds[1])
	upper, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], lower = %d, upper = %d\n", IntArrayToString(nums), lower, upper)

	timeStart := time.Now()

	result := countRangeSum(nums, lower, upper)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
