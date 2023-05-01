package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func maximizeSum(nums []int, k int) int {
	// 23ms
	return myMax(nums)*k + (k-1)*k/2
}

func myMax(nums []int) int {
	res := math.MinInt64
	for _, n := range nums {
		if n > res {
			res = n
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := maximizeSum(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
