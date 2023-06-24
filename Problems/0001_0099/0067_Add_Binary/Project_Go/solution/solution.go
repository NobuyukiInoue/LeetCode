package solution

import (
	"fmt"
	"strings"
	"time"
)

func addBinary(a string, b string) string {
	// 5ms
	ans := ""
	carry := 0
	i, j := len(a)-1, len(b)-1
	for (i >= 0) || (j >= 0) || carry != 0 {
		if i >= 0 {
			carry += int(a[i] - '0')
			i--
		}
		if j >= 0 {
			carry += int(b[j] - '0')
			j--
		}
		ans = string(carry%2+'0') + ans
		carry /= 2
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	a, b := flds[0], flds[1]
	fmt.Printf("a = \"%s\", b = \"%s\"\n", a, b)

	timeStart := time.Now()

	result := addBinary(a, b)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
