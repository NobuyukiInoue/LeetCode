package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func getFinalState(nums []int, k int, multiplier int) []int {
	// 0ms
	for k > 0 {
		n, v_min := 0, math.MaxInt64
		for i, num := range nums {
			if num < v_min {
				n, v_min = i, num
			}
		}
		nums[n] *= multiplier
		k--
	}
	return nums
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
	multiplier, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = %s, k = %d, multiplier = %d\n", IntArrayToString(nums), k, multiplier)

	timeStart := time.Now()

	result := getFinalState(nums, k, multiplier)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
