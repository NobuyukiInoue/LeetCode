package main

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func longestWord(words []string) string {
	sort.Sort(sort.StringSlice(words))
	m := map[string]int{"": 0}
	res := ""
	for _, word := range words {
		last_char_str := word[0 : len(word)-1]
		_, ok := m[last_char_str]
		if len(word) == 1 || ok {
			if len(word) > len(res) {
				res = word
			}
			m[word] = 1
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")

	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := longestWord(words)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
