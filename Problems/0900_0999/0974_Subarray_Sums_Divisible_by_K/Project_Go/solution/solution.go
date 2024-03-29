package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func subarraysDivByK(nums []int, k int) int {
	// 30ms - 32ms
	mod := make([]int, k)
	mod[0] = 1
	running_mod := 0
	for _, num := range nums {
		running_mod = (num + running_mod) % k
		for running_mod < 0 {
			running_mod += k
		}
		mod[running_mod]++
	}
	ans := 0
	for _, m := range mod {
		ans += m * (m - 1) / 2
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

	result := subarraysDivByK(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
