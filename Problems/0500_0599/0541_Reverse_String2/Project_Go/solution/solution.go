package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func reverseStr(s string, k int) string {
	ca := []rune(s)
	for left := 0; left < len(ca); left += 2 * k {
		for i, j := left, IntMin(left+k-1, len(ca)-1); i < j; i, j = i+1, j-1 {
			ca[i], ca[j] = ca[j], ca[i]
		}
	}
	return string(ca)
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	s := flds[0]
	k, _ := strconv.Atoi(flds[1])

	fmt.Printf("s = %s, k = %d\n", s, k)

	timeStart := time.Now()

	result := reverseStr(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
