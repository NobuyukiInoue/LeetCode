package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maxSubsequence(nums []int, k int) []int {
	// 5ms
	n := len(nums)
	ans := []int{}
	tmp := make([][2]int, n)

	for i, v := range nums {
		tmp[i][0], tmp[i][1] = v, i
	}

	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	sort.Slice(tmp, func(i, j int) bool { return tmp[i][0] > tmp[j][0] })
	tmp = tmp[:k]
	sort.Slice(tmp, func(i, j int) bool { return tmp[i][1] < tmp[j][1] })

	for _, v := range tmp {
		ans = append(ans, v[0])
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
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := maxSubsequence(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
