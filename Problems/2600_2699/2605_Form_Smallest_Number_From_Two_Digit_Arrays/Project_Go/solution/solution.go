package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
	//	"golang.org/x/exp/slices"
)

/*
func minNumber(nums1 []int, nums2 []int) int {
	sort.Sort(sort.IntSlice(nums1))
	sort.Sort(sort.IntSlice(nums2))
	for _, n := range nums1 {
		if slices.Contains(nums2, n) {
			return n
		}
	}
	if nums1[0] < nums2[0] {
		return 10*nums1[0] + nums2[0]
	}
	return 10*nums2[0] + nums1[0]
}
*/

func minNumber(nums1 []int, nums2 []int) int {
	// 0ms - 4ms
	sort.Sort(sort.IntSlice(nums1))
	sort.Sort(sort.IntSlice(nums2))
	for _, n := range nums1 {
		if contains(nums2, n) {
			return n
		}
	}
	if nums1[0] < nums2[0] {
		return 10*nums1[0] + nums2[0]
	}
	return 10*nums2[0] + nums1[0]
}

func contains(nums []int, target int) bool {
	for _, n := range nums {
		if n == target {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])

	fmt.Printf("nums1 = %s, nums2 = %s\n", IntArrayToString(nums1), IntArrayToString(nums2))

	timeStart := time.Now()

	result := minNumber(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
