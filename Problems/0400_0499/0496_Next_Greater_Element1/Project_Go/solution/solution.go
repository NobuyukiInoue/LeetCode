package solution

import (
	"fmt"
	"strings"
	"time"
)

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	mp := make(map[int]int)
	for i := 0; i < len(nums2); i++ {
		mp[nums2[i]] = i
	}

	var result []int
	for i := 0; i < len(nums1); i++ {
		key := mp[nums1[i]]
		for j := key; j < len(nums2); j++ {
			if nums2[j] > nums1[i] {
				result = append(result, nums2[j])
				break
			}
			if j == len(nums2)-1 {
				result = append(result, -1)
			}
		}

	}

	return result
}

func nextGreaterElement_work_bug(nums1 []int, nums2 []int) []int {
	dic := make(map[int]int)
	st := make([]int, 0)

	for _, num := range nums2 {
		if len(st) == 0 {
			st = append(st, num)
		} else if num <= st[len(st)-1] {
			st = append(st, num)
		} else {
			for len(st) > 0 && len(st) < num {
				dic[st[len(st)-1]] = num
				st = st[:len(st)-1]
			}
			st = append(st, num)
		}
	}

	result := make([]int, 0)
	for _, num := range nums1 {
		value, ok := dic[num]
		if ok == true {
			result = append(result, value)
		} else {
			result = append(result, -1)
		}
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	fmt.Printf("nums1 = [%s]\n", IntArrayToString(nums1))
	fmt.Printf("nums2 = [%s]\n", IntArrayToString(nums2))

	timeStart := time.Now()

	result := nextGreaterElement(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
