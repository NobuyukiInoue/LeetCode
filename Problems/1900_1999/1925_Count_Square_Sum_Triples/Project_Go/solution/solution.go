package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countTriples(n int) int {
	// 4ms
	ans := 0
	nums := make([]int, n+1)
	for i := 0; i <= n; i++ {
		nums[i] = i
	}
	for i := n; i >= 1; i-- {
		l, r := 0, i-1
		for l < r {
			if nums[l]*nums[l]+nums[r]*nums[r] == nums[i]*nums[i] {
				ans += 2
				l++
				r--
			} else if nums[l]*nums[l]+nums[r]*nums[r] < nums[i]*nums[i] {
				l++
			} else {
				r--
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := countTriples(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
