package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isFascinating(n int) bool {
	// 0ms
	var cnts [11]bool
	arr := []int{n, 2 * n, 3 * n}
	for _, cur := range arr {
		for temp := cur; temp > 0; temp /= 10 {
			if cnts[temp%10] == true || temp%10 == 0 {
				return false
			}
			cnts[temp%10] = true
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := isFascinating(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
