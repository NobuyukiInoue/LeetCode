package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumCounts(nums []int) int {
	// 218ms - 232ms
	ans, m := 0, len(nums)
	for i := 0; i < m; i++ {
		for j := i; j < m; j++ {
			mp := map[int]bool{}
			for k := i; k <= j; k++ {
				mp[nums[k]] = true
			}
			temp := len(mp)
			ans += temp * temp
		}
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

	result := sumCounts(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
