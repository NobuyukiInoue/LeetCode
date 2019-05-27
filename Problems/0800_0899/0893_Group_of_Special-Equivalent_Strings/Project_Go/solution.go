package main

import (
	"fmt"
	"strings"
	"time"
)

func numSpecialEquivGroups(A []string) int {
	m := map[[26]int]bool{}
	for _, s := range A {
		key := [26]int{}
		for i, ch := range s {
			if i%2 == 0 {
				key[byte(ch)-'a'] += 1
			} else {
				key[byte(ch)-'a'] += 100
			}
		}
		m[key] = true
	}
	return len(m)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	A := strings.Split(temp, ",")

	fmt.Printf("A = %s\n", A)

	timeStart := time.Now()

	result := numSpecialEquivGroups(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
