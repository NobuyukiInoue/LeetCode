package solution

import (
	"fmt"
	"strings"
	"time"
)

func findDifference(nums1 []int, nums2 []int) [][]int {
	// 24ms - 44ms
	check1, check2 := []int{}, []int{}
	nums1Set, nums2Set := map[int]struct{}{}, map[int]struct{}{}
	for _, num := range nums1 {
		nums1Set[num] = struct{}{}
	}
	for _, num := range nums2 {
		nums2Set[num] = struct{}{}
	}
	for num, _ := range nums1Set {
		if _, ok := nums2Set[num]; !ok {
			check1 = append(check1, num)
		}
	}
	for num, _ := range nums2Set {
		if _, ok := nums1Set[num]; !ok {
			check2 = append(check2, num)
		}
	}
	return [][]int{check1, check2}
}

func findDifference2(nums1 []int, nums2 []int) [][]int {
	// 54ms - 66ms
	check1, check2 := make(map[int]bool), make(map[int]bool)
	for _, num := range nums1 {
		check1[num] = true
	}
	for _, num := range nums2 {
		check2[num] = true
	}

	result := make([][]int, 2)
	for num := range check1 {
		if _, ok := check2[num]; !ok {
			result[0] = append(result[0], num)
		}
	}
	for num := range check2 {
		if _, ok := check1[num]; !ok {
			result[1] = append(result[1], num)
		}
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	nums := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		nums[i] = StringToIntArray(str_mat[i])
	}
	nums1, nums2 := nums[0], nums[1]
	fmt.Printf("nums1 = [%s], nums2 = [%s]\n", IntArrayToString(nums1), IntArrayToString(nums2))

	timeStart := time.Now()

	result := findDifference(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
