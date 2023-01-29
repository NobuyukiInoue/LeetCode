package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func alternateDigitSum(n int) int {
	// 0ms - 1ms
	sign, cnt, ans := 1, 0, 0
	for n > 0 {
		ans += sign * (n % 10)
		n /= 10
		sign *= -1
		cnt++
	}
	if cnt%2 == 1 {
		return ans
	}
	return -ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := alternateDigitSum(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
