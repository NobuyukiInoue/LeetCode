package solution

import (
	"fmt"
	"strings"
	"time"
)

func countBadPairs(nums []int) int64 {
	// 127ms - 142ms
	count_dict := make(map[int]int, 0)
	var ans int64
	for i, _ := range nums {
		prev := count_dict[i-nums[i]]
		ans += int64(i - prev)
		count_dict[i-nums[i]] = prev + 1
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countBadPairs(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
