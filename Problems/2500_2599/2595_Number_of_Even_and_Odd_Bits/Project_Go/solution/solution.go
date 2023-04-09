package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func evenOddBit(n int) []int {
	// 0ms
	ans := []int{0, 0}
	odd := false
	for n > 0 {
		if !odd {
			if n&1 == 1 {
				ans[0]++
			}
			odd = true
		} else {
			if n&1 == 1 {
				ans[1]++
			}
			odd = false
		}
		n >>= 1
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := evenOddBit(n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
