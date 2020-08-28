package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func thousandSeparator(n int) string {
	// 0ms
	num := strconv.Itoa(n)
	res := ""
	for i := len(num); i > 0; i -= 3 {
		if len(res) > 0 {
			res = "." + res
		}
		if i-3 > 0 {
			res = num[i-3:i] + res
		} else {
			res = num[0:i] + res
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := thousandSeparator(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
