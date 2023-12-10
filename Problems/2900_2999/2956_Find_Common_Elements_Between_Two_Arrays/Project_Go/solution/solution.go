package solution

import (
	"fmt"
	"slices"
	"strings"
	"time"
)

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	// 7ms - 23ms
	res1, res2 := 0, 0
	for _, num := range nums1 {
		if slices.Contains(nums2, num) {
			res1++
		}
	}
	for _, num := range nums2 {
		if slices.Contains(nums1, num) {
			res2++
		}
	}
	return []int{res1, res2}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	fmt.Printf("nums1 = [%s], nums2 = [%s]\n", IntArrayToString(nums1), IntArrayToString(nums2))

	timeStart := time.Now()

	result := findIntersectionValues(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
