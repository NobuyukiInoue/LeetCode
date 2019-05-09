package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	front, back := 0, len(s)-1
	for front <= back {
		if (s[front] >= 'a' && s[front] <= 'z') || (s[front] >= '0' && s[front] <= '9') {
			if (s[back] >= 'a' && s[back] <= 'z') || (s[back] >= '0' && s[back] <= '9') {
				if s[front] != s[back] {
					return false
				}
				front++
				back--
			} else {
				back--
			}
		} else {
			front++
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := isPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
