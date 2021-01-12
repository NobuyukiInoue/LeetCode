package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxSlidingWindow(nums []int, k int) []int {
	// 200ms
	q := make([]int, 0)
	res := make([]int, len(nums) - k + 1)
	pos := 0
	for i := 0; i < len(nums); i++ {
		if i - k >= 0 {
			res[pos] = nums[q[0]]
			pos++
			for len(q) > 0 && q[0] <= i - k {
				q = q[1:]
			}
		}
		for len(q) > 0 && nums[i] > nums[q[len(q) -1]] {
			q = q[:len(q) - 1]
		}
		q = append(q, i)
	}
	res[pos] = nums[q[0]]
	return res
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
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := maxSlidingWindow(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
