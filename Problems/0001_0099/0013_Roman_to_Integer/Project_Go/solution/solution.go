package solution

import (
	"fmt"
	"strings"
	"time"
)

var m = map[uint8] int {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000,
}

func romanToInt(s string) int {
	// 8ms
    var result int

	prev := s[0]
	value := m[prev]

	for i:= 1; i < len(s); i++ {
		c := s[i]
		v := m[c]

		if v > m[prev] {
			prev = c
			result += v - value
			value = 0

			continue
		}

		prev = c
		result += value
		value = v
	}	

	return result + value
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
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := romanToInt(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
