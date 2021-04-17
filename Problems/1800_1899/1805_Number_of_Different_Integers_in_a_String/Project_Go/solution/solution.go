package solution

import (
	"fmt"
	"strings"
	"time"
)

func numDifferentIntegers(word string) int {
	// 0ms
	targets := make([]string, 0)
	i := 0
	wordLen := len(word)
	for i < wordLen {
	  ch := word[i]
	  if '0' <= ch && ch <= '9' {
		end := i
		for end < wordLen && '0' <= word[end] && word[end] <= '9' {
			end++
		}
		for i < end && word[i] == '0' {
			i++
		}
		target := word[i:end]
		if !contains(targets, target) {
			targets = append(targets, target)
		}
		i = end + 1
		} else {
			i++;
		}
	}
	fmt.Printf("%s\n", targets)
	return len(targets)
}

func contains(s []string, e string) bool {
	for _, v := range s {
		if e == v {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := numDifferentIntegers(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
