package main

import (
	"fmt"
	"strings"
	"time"
)

func countCharacters(words []string, chars string) int {
	// 12ms
	charmap := [26]int{}
	m := [26]int{}
	mastered := 0
	for _, c := range []byte(chars) {
		charmap[c-'a'] += 1
	}

	count := 0
	for _, word := range words {
		count = len(word)
		for i := range m {
			m[i] = charmap[i]
		}
		for _, c := range []byte(word) {
			if m[c-'a'] > 0 {
				m[c-'a'] -= 1
			} else {
				count = 0
				break
			}
		}
		mastered += count
	}
	return mastered
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	words := strings.Split(flds[0], ",")
	chars := flds[1]

	fmt.Printf("words = %s, chars = %s\n", words, chars)
	timeStart := time.Now()

	result := countCharacters(words, chars)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
