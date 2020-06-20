package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func summaryRanges(nums []int) []string {
	// 0ms
	var res []string

	if nums == nil || len(nums) == 0 {
		return res
	}

	for i := 0; i < len(nums); i++ {
		j := i + 1
		for j < len(nums) && nums[j] == nums[j-1]+1 {
			j++
		}
		if j-i-1 >= 1 {
			res = append(res, strconv.Itoa(nums[i])+"->"+strconv.Itoa(nums[j-1]))
		} else {
			res = append(res, strconv.Itoa(nums[i]))
		}
		i = j - 1
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

	result := summaryRanges(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
