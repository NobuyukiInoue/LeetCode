package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findKOr(nums []int, k int) int {
	// 0ms
	ans := 0
	for i := 0; i < 31; i++ {
		rep := (1 << i)
		cnt := 0
		for _, num := range nums {
			if (rep & num) != 0 {
				cnt++
			}
		}
		if cnt >= k {
			ans += rep
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

	result := findKOr(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
