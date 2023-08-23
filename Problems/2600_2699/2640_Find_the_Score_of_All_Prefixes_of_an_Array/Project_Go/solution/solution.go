package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findPrefixScore(nums []int) []int64 {
	// 86ms - 100ms
	n := len(nums)
	ans := make([]int64, n+1)
	t_max := 0
	for i := 0; i < n; i++ {
		t_max = myMax(t_max, nums[i])
		ans[i+1] = int64(nums[i]) + int64(t_max) + ans[i]
	}
	return ans[1:]
}

func findPrefixScore2(nums []int) []int64 {
	// 95ms
	n := len(nums)
	ans := []int64{int64(nums[0] * 2)}
	t_max := nums[0]
	for i := 1; i < n; i++ {
		t_max = myMax(t_max, nums[i])
		ans = append(ans, int64(ans[len(ans)-1]+int64(t_max+nums[i])))
	}
	return ans
}

func myMax(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func Int64ArrayToString(nums []int64) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatInt(nums[0], 10)
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatInt(nums[i], 10)
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findPrefixScore(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", Int64ArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
