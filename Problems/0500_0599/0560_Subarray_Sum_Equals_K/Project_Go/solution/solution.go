package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func subarraySum(nums []int, k int) int {
	// 44ms
	preSums := map[int]int{}
	preSums[0] = 1
	s, res := 0, 0
	for _, num := range nums {
		s += num
		res += preSums[s-k]
		preSums[s] = preSums[s] + 1
	}
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

	result := subarraySum(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
