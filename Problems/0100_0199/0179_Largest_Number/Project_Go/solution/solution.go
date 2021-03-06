package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func largestNumber(nums []int) string {
	// 4ms
	if nums == nil || len(nums) == 0 {
		return ""
	}

	s_nums := make([]string, len(nums))

	for i := 0; i < len(nums); i++ {
		s_nums[i] = strconv.Itoa(nums[i])
	}

	sort.Slice(s_nums, func(i, j int) bool {
		a, _ := strconv.Atoi(s_nums[i] + s_nums[j])
		b, _ := strconv.Atoi(s_nums[j] + s_nums[i])
		if a >= b {
			return true
		}
		return false
	})

	if s_nums[0][0] == '0' {
		return "0"
	}

	/*
		res := s_nums[0]
		for i := 1; i < len(s_nums); i++ {
			res += s_nums[i]
		}
		return res
	*/
	return strings.Join(s_nums, "")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := largestNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
