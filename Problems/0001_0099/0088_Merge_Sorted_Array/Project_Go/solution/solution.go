package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	// 0ms
	i := m - 1
	j := n - 1
	k := m + n - 1
	for j >= 0 {
		if i >= 0 && nums1[i] > nums2[j] {
			nums1[k] = nums1[i]
			k--
			i--
		} else {
			nums1[k] = nums2[j]
			k--
			j--
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]][", "", -1)
	flds := strings.Split(temp, "]],[[")
	flds1 := strings.Split(flds[0], "],[")
	flds2 := strings.Split(flds[1], "],[")

	nums1 := StringToIntArray(flds1[0])
	m, _ := strconv.Atoi(flds1[1])
	nums2 := StringToIntArray(flds2[0])
	n, _ := strconv.Atoi(flds2[1])
	fmt.Printf("nums1 = [%s], m = %d\n", IntArrayToString(nums1), m)
	fmt.Printf("nums2 = [%s], n = %d\n", IntArrayToString(nums2), n)

	timeStart := time.Now()

	merge(nums1, m, nums2, n)

	timeEnd := time.Now()

	fmt.Printf("==== result ====\n")
	fmt.Printf("nums1 = [%s]\n", IntArrayToString(nums1))
	fmt.Printf("nums1 = [%s]\n", IntArrayToString(nums2))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
