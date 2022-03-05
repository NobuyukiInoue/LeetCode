package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func sortEvenOdd(nums []int) []int {
	// 3ms
	evenRight, oddRight := len(nums)-2, len(nums)-1
	if evenRight&1 == 1 {
		evenRight, oddRight = oddRight, evenRight
	}

	quickSort(nums, 0, evenRight, 2, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	quickSort(nums, 1, oddRight, 2, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	return nums
}

func quickSort(arr []int, low, high, step int, comparer func(i, j int) bool) {
	if low < high {
		p := partition(arr, low, high, step, comparer)
		quickSort(arr, low, p-step, step, comparer)
		quickSort(arr, p+step, high, step, comparer)
	}
}

func partition(arr []int, low, high, step int, comparer func(i, j int) bool) int {
	for j := low; j < high; j += step {
		if comparer(j, high) {
			arr[low], arr[j] = arr[j], arr[low]
			low += step
		}
	}

	arr[low], arr[high] = arr[high], arr[low]
	return low
}

func sortEvenOdd2(nums []int) []int {
	// 5ms
	n := len(nums)
	en, on := (n+1)/2, n/2
	evens, odds := make([]int, en), make([]int, on)

	for i := range evens {
		evens[i] = nums[i*2]
	}
	for i := range odds {
		odds[i] = nums[i*2+1]
	}

	sort.Ints(evens)
	sort.Slice(odds, func(i, j int) bool { return odds[i] > odds[j] })

	for i, even := range evens {
		nums[i*2] = even
	}
	for i, odd := range odds {
		nums[i*2+1] = odd
	}
	return nums
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := sortEvenOdd(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
