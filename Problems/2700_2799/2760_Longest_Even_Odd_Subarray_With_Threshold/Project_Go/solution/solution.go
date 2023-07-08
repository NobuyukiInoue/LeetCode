package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func longestAlternatingSubarray(nums []int, threshold int) int {
	// 58ms - 72m
	ans, cnt, parity := 0, 0, 0
	for _, num := range nums {
		if num > threshold {
			cnt = 0
		} else if cnt >= 1 && parity != num%2 {
			parity ^= 1
			cnt++
		} else {
			parity = num % 2
			cnt = parity ^ 1
		}
		ans = myMax(ans, cnt)
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	threshold, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], threshold = %d\n", IntArrayToString(nums), threshold)

	timeStart := time.Now()

	result := longestAlternatingSubarray(nums, threshold)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
