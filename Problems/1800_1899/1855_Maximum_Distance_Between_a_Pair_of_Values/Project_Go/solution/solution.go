package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDistance(nums1 []int, nums2 []int) int {
	// 152ms
	i, res := 0, 0
	m, n := len(nums1), len(nums2)
	for j := 0; j < n; j++ {
		for i < m && nums1[i] > nums2[j] {
			i++
		}
		if i == m {
			break
		}
		res = myMax(res, j-i)
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
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
	fmt.Printf("nums1 = %s\n", IntArrayToString(nums1))
	fmt.Printf("nums2 = %s\n", IntArrayToString(nums2))

	timeStart := time.Now()

	result := maxDistance(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
