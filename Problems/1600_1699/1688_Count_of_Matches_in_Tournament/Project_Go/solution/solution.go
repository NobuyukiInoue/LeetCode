package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfMatches(n int) int {
	// 0ms
	res := 0
	var matches int
	for n > 1 {
		if n % 2 == 1 {
			matches = n / 2
			n = matches + 1
		} else {
			matches = n / 2
			n = matches
		}
		res += matches
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

	result := numberOfMatches(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
