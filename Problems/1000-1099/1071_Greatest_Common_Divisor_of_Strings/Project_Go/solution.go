package main

import (
	"fmt"
	"strings"
	"time"
)

func gcdOfStrings(str1 string, str2 string) string {
	l1, l2 := len(str1), len(str2)
	d := gcd(max(l1, l2), min(l1, l2))
	p := str2[:d]
	if str1 == strings.Repeat(p, l1/d) && str2 == strings.Repeat(p, l2/d) {
		return p
	}
	return ""
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	str1, str2 := flds[0], flds[1]

	fmt.Printf("str1 = %s, str2 = %s\n", str1, str2)

	timeStart := time.Now()

	result := gcdOfStrings(str1, str2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
