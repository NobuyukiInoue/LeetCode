package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lastRemaining(n int) int {
	if n == 1 {
		return 1
	}
	if n <= 3 {
		return 2
	}
	if (n/2)%2 == 1 {
		return 4 * lastRemaining((n-2)/4)
	} else {
		return 4*lastRemaining(n/4) - 2
	}
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

	result := lastRemaining(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
