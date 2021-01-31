package solution

import (
	"fmt"
	"strings"
	"time"
)

func countSubstrings(s string) int {
	// 0ms
	sLen := len(s)
	res := sLen
	for i := 1; i < sLen; i++ {
		for j := 1; j < myMin(sLen-i-1, i)+1; j++ {
			if s[i-j] == s[i+j] {
				res++
			} else {
				break
			}
		}
		if s[i] == s[i-1] {
			res++
			for j := 1; j < myMin(i-1, sLen-i-1)+1; j++ {
				if s[i+j] == s[i-1-j] {
					res++
				} else {
					break
				}
			}
		}
	}
	return res
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := countSubstrings(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
