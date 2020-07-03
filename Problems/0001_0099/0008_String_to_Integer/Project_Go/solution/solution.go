package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func myAtoi(str string) int {
	// 0ms
	str = strings.Trim(str, " ")
	neg := false
	x := 0

   for i := 0; i < len(str); i++ {
		if i == 0 && str[0] == '-' {
			neg = true
			continue
		}
		if i == 0 && str[0] == '+' {
			continue
		}
		if str[i] < '0' || str[i] > '9' {
			break
		}
		x = x * 10 + (int(str[i]) - '0')
		if x > math.MaxInt32 {
			if neg {
				return math.MinInt32
			} else {
				return math.MaxInt32
			}
		}
	}

	if neg {
		return -1 * int(x)
	} else {
		return int(x)
	}
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
	str := strings.Replace(temp, "]", "", -1)
	fmt.Printf("str = \"%s\"\n", str)

	timeStart := time.Now()

	result := myAtoi(str)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
