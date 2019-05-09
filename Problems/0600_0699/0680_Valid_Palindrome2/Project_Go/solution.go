package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func validPalindrome(s string) bool {
	valid := func(s string, l int, r int) bool {
		for l < r {
			if s[l] != s[r] {
				return false
			}
			l++
			r--
		}
		return true
	}
	for l, r := 0, len(s)-1; l < r; {
		if s[l] != s[r] {
			return valid(s, l, r-1) || valid(s, l+1, r)
		}
		l++
		r--
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := validPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
