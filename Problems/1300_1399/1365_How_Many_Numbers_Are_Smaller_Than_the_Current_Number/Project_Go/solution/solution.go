package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func smallerNumbersThanCurrent(nums []int) []int {
	// 4ms
	numsCopy := make([]int, len(nums))
	copy(numsCopy, nums)
	sort.Sort(sort.IntSlice(numsCopy))
	res := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		res[i] = binarySearch(numsCopy, nums[i])
	}

	return res
}

func binarySearch(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return l
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

	result := smallerNumbersThanCurrent(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
