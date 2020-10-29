package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func integerReplacement(n int) int {
	// 0ms
	ans := 0
	for n != 1 {
		if (n & 1) == 0 {
			n >>= 1
		} else if n == 3 || ((n + 1) & n) > ((n - 1) & (n - 2)) {
			n--
		} else {
			n++
		}
		ans++
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := integerReplacement(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
