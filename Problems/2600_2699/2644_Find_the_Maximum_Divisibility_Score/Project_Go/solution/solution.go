package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDivScore(nums []int, divisors []int) int {
	// 908ms - 912ms
	ans, max_cnt := -1, -1
	for _, divisor := range divisors {
		cnt := 0
		for _, num := range nums {
			if num%divisor == 0 {
				cnt++
			}
		}
		if cnt > max_cnt {
			max_cnt = cnt
			ans = divisor
		} else if cnt == max_cnt {
			ans = myMin(ans, divisor)
		}
	}
	return ans
}

func myMin(a, b int) int {
	if a <= b {
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
	divisors := StringToIntArray(flds[1])

	fmt.Printf("nums = [%s], divisors = [%s]\n", IntArrayToString(nums), IntArrayToString(divisors))

	timeStart := time.Now()

	result := maxDivScore(nums, divisors)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
