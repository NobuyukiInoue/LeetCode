package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasIncreasingSubarrays(nums []int, k int) bool {
	// 7ms - 11ms
	cnt, pre_max_cnt, res := 1, 0, 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			cnt++
		} else {
			pre_max_cnt, cnt = cnt, 1
		}
		res = myMax(res, myMax(cnt/2, myMin(pre_max_cnt, cnt)))
	}
	return res >= k
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := hasIncreasingSubarrays(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
