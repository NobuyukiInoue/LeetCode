package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isBalanced(num string) bool {
	// 0ms
	v_sum, sign := 0, 1
	for _, n := range num {
		v_sum += sign * (int(n) - '0')
		sign *= -1
	}
	return v_sum == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = \"%s\"\n", num)

	timeStart := time.Now()

	result := isBalanced(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
