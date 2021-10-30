package solution

import (
	"fmt"
	"strings"
	"time"
)

func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	// 4ms
	list := make([]int, 0)
	count := make([][]int, 3)
	for i := 0; i < len(count); i++ {
		count[i] = make([]int, 101)
	}
	for _, n := range nums1 {
		count[0][n] = 1
	}
	for _, n := range nums2 {
		count[1][n] = 1
	}
	for _, n := range nums3 {
		count[2][n] = 1
	}
	for i := 1; i <= 100; i++ {
		if count[0][i]+count[1][i]+count[2][i] > 1 {
			list = append(list, i)
		}
	}
	return list
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
	nums3 := StringToIntArray(flds[2])
	fmt.Printf("nums1 = [%s], nums2 = [%s], nums3 = [%s]\n", IntArrayToString(nums1), IntArrayToString(nums2), IntArrayToString(nums3))

	timeStart := time.Now()

	result := twoOutOfThree(nums1, nums2, nums3)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
