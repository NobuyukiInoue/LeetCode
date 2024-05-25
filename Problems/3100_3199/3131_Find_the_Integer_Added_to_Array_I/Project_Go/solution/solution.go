package solution

import (
	"fmt"
	"strings"
	"time"
)

func addedInteger(nums1 []int, nums2 []int) int {
	// 0ms
	min1, min2 := nums1[0], nums2[0]
	for i := 1; i < len(nums1); i++ {
		min1 = myMin(min1, nums1[i])
		min2 = myMin(min2, nums2[i])
	}
	return min2 - min1
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	fmt.Printf("nums1 = %s, nums2 = %s\n", IntArrayToString(nums1), IntArrayToString(nums2))

	timeStart := time.Now()

	result := addedInteger(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
