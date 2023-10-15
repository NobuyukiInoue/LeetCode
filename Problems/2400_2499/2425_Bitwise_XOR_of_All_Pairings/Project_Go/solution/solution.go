package solution

import (
	"fmt"
	"strings"
	"time"
)

func xorAllNums(nums1 []int, nums2 []int) int {
	// 99ms - 100ms
	x, y := 0, 0
	for _, num1 := range nums1 {
		x ^= num1
	}
	for _, num2 := range nums2 {
		y ^= num2
	}
	return (len(nums1) % 2 * y) ^ (len(nums2) % 2 * x)
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

	result := xorAllNums(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
