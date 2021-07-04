package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func reinitializePermutation(n int) int {
	// 0ms
	res, i := 0, 1
	for res == 0 || i > 1 {
		if i < n/2 {
			i *= 2
		} else {
			i = (i-n/2)*2 + 1
		}
		res++
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := reinitializePermutation(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
