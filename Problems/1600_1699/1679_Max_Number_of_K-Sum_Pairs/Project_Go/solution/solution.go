package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maxOperations_use_sort(nums []int, k int) int {
	// 114ms - 134ms
	low, high, minOpe := 0, len(nums)-1, 0
	sort.Ints(nums)
	for low < high {
		if nums[low]+nums[high] == k {
			minOpe++
			low++
			high--
		} else if nums[low]+nums[high] > k {
			high--
		} else {
			low++
		}
	}
	return minOpe
}

func maxOperations(nums []int, k int) int {
	// 93ms - 110ms
	cnts, ans := make(map[int]int, 0), 0
	for _, num := range nums {
		cnts[num]++
	}
	for key, _ := range cnts {
		ans += myMin(cnts[key], cnts[k-key])
	}
	return ans / 2
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := maxOperations(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
