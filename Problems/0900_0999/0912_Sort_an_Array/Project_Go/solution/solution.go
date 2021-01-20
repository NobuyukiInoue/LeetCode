package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func sortArrayDefault(nums []int) []int {
	// 24ms
	sort.Sort(sort.IntSlice(nums))
	return nums
}

func sortArray(nums []int) []int {
	// 20ms
	quicksort(nums, 0, len(nums) - 1)
	return nums
}

func partition(nums []int, left int, right int) int {
	pivot := nums[right]
	start := left
	end := right - 1
	for start <= end {
		if (nums[start] < pivot) {
			start++
		} else if (nums[end] >= pivot) {
			end--
		} else {
			nums[start], nums[end] = nums[end], nums[start]
			start++
			end--
		}
	}
	nums[start], nums[right] = nums[right], nums[start]
	return start
}

func quicksort(nums []int, left int, right int) {
	if left >= right {
		return
	}
	pivot := partition(nums, left, right)
	quicksort(nums, left, pivot - 1)
	quicksort(nums, pivot + 1, right)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := sortArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
