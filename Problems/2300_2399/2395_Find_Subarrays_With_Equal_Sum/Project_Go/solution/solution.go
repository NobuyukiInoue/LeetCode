package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findSubarrays(nums []int) bool {
	// 2ms - 8ms
	hm := make(map[int]int, 0)
	for i := 0; i < len(nums)-1; i++ {
		t := nums[i] + nums[i+1]
		if _, ok := hm[t]; ok {
			return true
		}
		hm[t] = 1
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findSubarrays(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
