package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func threeSum(nums []int) [][]int {
	// 28ms
	sort.Sort(sort.IntSlice(nums))
	res := make([][]int, 0)
	for i := 0; i < len(nums) - 2; i++ {
		if i > 0 && nums[i] == nums[i - 1] {
			continue
		}
		l, r := i + 1, len(nums) - 1
		for l < r {
			s := nums[l] + nums[i] + nums[r];
			if s > 0 {
				r--
			} else if s < 0 {
				l++
			} else {
				res = append(res, []int {nums[l], nums[i], nums[r]})
				for l < r && nums[l] == nums[l+1] {
					l++
				}
				for l < r && nums[r] == nums[r-1] {
					r--
				}
				l, r = l + 1, r - 1
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := threeSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
