package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfPairs(nums1 []int, nums2 []int, k int) int {
	// 0ms
	ans := 0
	for _, num1 := range nums1 {
		for _, num2 := range nums2 {
			if num1%(num2*k) == 0 {
				ans++
			}
		}
	}
	return ans
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
	k, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums1 = %s, nums2 = %s, k = %d\n", IntArrayToString(nums1), IntArrayToString(nums2), k)

	timeStart := time.Now()

	result := numberOfPairs(nums1, nums2, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
