package solution

import (
	"fmt"
	"strings"
	"time"
)

func getCommon(nums1 []int, nums2 []int) int {
	// 76ms - 77ms
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			i++
		} else if nums1[i] > nums2[j] {
			j++
		} else {
			return nums1[i]
		}
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	fmt.Printf("nums1 = [%s]\n", IntArrayToString(nums1))
	fmt.Printf("nums2 = [%s]\n", IntArrayToString(nums2))

	timeStart := time.Now()

	result := getCommon(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
