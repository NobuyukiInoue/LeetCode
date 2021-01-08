package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func findDuplicates(nums []int) []int {
	// 52ms
	var res []int
	for i := 0; i < len(nums); i++ {
		for nums[i] != i+1 {
			a := nums[i]
			if nums[a-1] == 0 {
				nums[i], nums[a-1] = nums[a-1], nums[i]
				break
			}
			if nums[a-1] == a {
				res = append(res, a)
				nums[i] = 0
				break
			}
			nums[i], nums[a-1] = nums[a-1], nums[i]
		}
	}
	return res
}

func findDuplicates2(nums []int) []int {
	// 84ms
	var res []int
	sort.Sort(sort.IntSlice(nums))

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			res = append(res, nums[i])
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findDuplicates(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
