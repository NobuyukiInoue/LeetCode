package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func compareVersion(version1 string, version2 string) int {
	// 0ms
	str1, str2 := strings.Split(version1, "."), strings.Split(version2, ".")
	nums1, nums2 := make([]int, len(str1)), make([]int, len(str2))

	for i := 0; i < len(nums1); i++ {
		nums1[i], _ = strconv.Atoi(str1[i])
	}

	for i := 0; i < len(nums2); i++ {
		nums2[i], _ = strconv.Atoi(str2[i])
	}

	var v1, v2 int
	for i := 0; i < myMax(len(nums1), len(nums2)); i++ {
		if i < len(nums1) {
			v1 = nums1[i]
		} else {
			v1 = 0
		}
		if i < len(nums2) {
			v2 = nums2[i]
		} else {
			v2 = 0
		}

		if v1 > v2 {
			return 1
		} else if v1 < v2 {
			return -1
		}
	}
	return 0
}

func myMax(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)

	flds := strings.Split(temp, ",")
	version1, version2 := flds[0], flds[1]
	fmt.Printf("version1 = %s, version2 = %s\n", version1, version2)

	timeStart := time.Now()

	result := compareVersion(version1, version2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
