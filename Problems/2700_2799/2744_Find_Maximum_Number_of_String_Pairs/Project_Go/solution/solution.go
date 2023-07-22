package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumNumberOfStringPairs(words []string) int {
	// 0ms
	var word_set []string
	ans := 0
	for _, word := range words {
		if contains(word_set, word) {
			ans++
		} else {
			word_set = append(word_set, reverse(word))
		}
	}
	return ans
}

func contains(strings []string, target string) bool {
	for _, s := range strings {
		if s == target {
			return true
		}
	}
	return false
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = [%s]\n", StringArrayToString(words))

	timeStart := time.Now()

	result := maximumNumberOfStringPairs(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
