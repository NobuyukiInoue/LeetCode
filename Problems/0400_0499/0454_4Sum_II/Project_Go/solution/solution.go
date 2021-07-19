package solution

import (
	"fmt"
	"strings"
	"time"
)

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	// 132ms
	cnt := map[int]int{}
	for _, a := range nums1 {
		for _, b := range nums2 {
			cnt[a+b]++
		}
	}
	ans := 0
	for _, c := range nums3 {
		for _, d := range nums4 {
			if _, ok := cnt[-(c + d)]; ok {
				ans += cnt[-(c + d)]
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

	nums := make([][]int, len(flds))
	for i := 0; i < len(nums); i++ {
		nums[i] = StringToIntArray(flds[i])
	}
	nums1, nums2, nums3, nums4 := nums[0], nums[1], nums[2], nums[3]
	fmt.Printf("nums1 = %s, nums2 = %s, nums3 = %s, nums4 = %s\n",
		IntArrayToString(nums1),
		IntArrayToString(nums2),
		IntArrayToString(nums3),
		IntArrayToString(nums4))

	timeStart := time.Now()

	result := fourSumCount(nums1, nums2, nums3, nums4)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
