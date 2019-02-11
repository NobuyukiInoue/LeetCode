package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	sum := len(nums1) + len(nums2)
	median := sum/2 + 1

	//add sentinel
	nums1 = append(nums1, int(^uint(0)>>1))
	nums2 = append(nums2, int(^uint(0)>>1))
	n := make([]int, median)
	j, k := 0, 0

	for i := 0; i < median; i++ {
		if nums1[j] < nums2[k] {
			n[i] = nums1[j]
			j++
		} else {
			n[i] = nums2[k]
			k++
		}
	}

	if sum%2 == 0 {
		return float64(n[median-1]+n[median-2]) / 2
	} else {
		return float64(n[median-1])
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums1 := str2IntArray(flds[0])
	nums2 := str2IntArray(flds[1])

	fmt.Printf("nums1 = %s\n", printIntArray(nums1))
	fmt.Printf("nums2 = %s\n", printIntArray(nums2))

	timeStart := time.Now()

	result := findMedianSortedArrays(nums1, nums2)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %d [ms]\n\n", timeEnd.Sub(timeStart)*1000)
}
