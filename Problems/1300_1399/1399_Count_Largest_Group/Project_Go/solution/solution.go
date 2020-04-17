package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countLargestGroup(n int) int {
	// 4ms
	res, max := 0, 0
	count := make(map[int]int)

	for i := 1; i <= n; i++ {
		sum, j := 0, i
		for j > 0 {
			sum += j % 10
			j /= 10
		}
		count[sum] = count[sum] + 1
		if max < count[sum] {
			max = count[sum]
			res = 1
		} else if max == count[sum] {
			res++
		}
	}
	return res
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

	result := countLargestGroup(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
