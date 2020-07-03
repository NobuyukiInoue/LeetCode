package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func reverse(x int) int {
	// 0ms
	rev := 0
	for x != 0 {
		pop := x % 10
		x /= 10
		if (rev > math.MaxInt32/10) || (rev == math.MaxInt32 / 10 && pop > 7) {
			return 0
		}
		if (rev < math.MinInt32/10) || (rev == math.MinInt32 / 10 && pop < -8) {
			return 0
		}
		rev = rev * 10 + pop
	}
	return rev
}

func checkPalindrome(s string, i int, j int, max string) string {
	leng := len(s)
	var sub string
	for i >= 0 && j <= (leng-1) && s[i] == s[j] {
		sub = s[i : j+1]
		i--
		j++
	}
	if len(max) < len(sub) {
		max = sub
	}
	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	x, _ := strconv.Atoi(fld);
	fmt.Printf("x = %d\n", x)

	timeStart := time.Now()

	result := reverse(x)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
