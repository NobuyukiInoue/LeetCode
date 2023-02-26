package solution

import (
	"fmt"
	"strings"
	"time"
)

func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	// 4ms
	var res [][]int
	i, j := 0, 0
	for i < len(nums1) || j < len(nums2) {
		if i == len(nums1) {
			res = append(res, nums2[j])
			j++
		} else if j == len(nums2) {
			res = append(res, nums1[i])
			i++
		} else {
			if nums1[i][0] == nums2[j][0] {
				res = append(res, []int{nums1[i][0], nums1[i][1] + nums2[j][1]})
				i++
				j++
			} else if nums1[i][0] < nums2[j][0] {
				res = append(res, nums1[i])
				i++
			} else {
				res = append(res, nums2[j])
				j++
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	flds0 := strings.Split(flds[0], "],[")
	nums1 := make([][]int, len(flds0))
	for i, _ := range flds0 {
		nums1[i] = StringToIntArray(flds0[i])
	}

	flds1 := strings.Split(flds[1], "],[")
	nums2 := make([][]int, len(flds1))
	for i, _ := range flds1 {
		nums2[i] = StringToIntArray(flds1[i])
	}

	fmt.Printf("nums1 = %s, nums2 = %s\n", IntIntArrayToString(nums1), IntIntArrayToString(nums2))

	timeStart := time.Now()

	result := mergeArrays(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
