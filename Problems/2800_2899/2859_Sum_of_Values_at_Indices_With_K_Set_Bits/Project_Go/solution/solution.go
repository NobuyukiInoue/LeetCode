package solution

import (
	"fmt"
	"math/bits"
	"strconv"
	"strings"
	"time"
)

func sumIndicesWithKSetBits(nums []int, k int) int {
	// 7ms - 11ms
	ans := 0
	for i, num := range nums {
		if bits.OnesCount(uint(i)) == k {
			ans += num
		}
	}
	return ans
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

	result := sumIndicesWithKSetBits(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
