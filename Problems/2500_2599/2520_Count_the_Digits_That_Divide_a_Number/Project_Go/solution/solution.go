package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countDigits(num int) int {
	// 0ms
	n, ans := num, 0
	for n > 0 {
		val := n % 10
		if num%val == 0 {
			ans++
		}
		n /= 10
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := countDigits(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
