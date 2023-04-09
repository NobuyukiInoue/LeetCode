package solution

import (
	"fmt"
	"strings"
	"time"
)

func findTheLongestBalancedSubstring(s string) int {
	// 0ms - 14ms
	temp, res := "01", 0
	for len(temp) <= len(s) {
		if strings.Contains(s, temp) {
			res = len(temp)
		}
		temp = "0" + temp + "1"
	}
	return res
}

func findTheLongestBalancedSubstring0(s string) int {
	// 4ms
	res, i := 0, 0
	for i < len(s) {
		z, o := 0, 0
		for i < len(s) && s[i] == '0' {
			z++
			i++
		}
		for i < len(s) && s[i] == '1' && z > o {
			o++
			i++
			res = myMax(res, o*2)
		}
		for i < len(s) && s[i] == '1' {
			i++
		}
	}
	return res
}

func myMax(a, b int) int {
	if a > b {
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

	result := findTheLongestBalancedSubstring(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
