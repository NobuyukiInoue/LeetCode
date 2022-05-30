package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeAnagrams(words []string) []string {
	// 0ms
	var result []string
	prevHash := 0
	for _, word := range words {
		curWord := word
		curHash := myHash(curWord)
		if curHash == prevHash {
			continue
		} else {
			result = append(result, curWord)
			prevHash = curHash
		}
	}
	return result
}

func myHash(s string) int {
	h := 1
	counts := make([]int, 26)
	for _, ch := range s {
		counts[ch-'a']++
	}
	for _, count := range counts {
		h *= 11
		h += count
	}
	return h
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = [%s]\n", StringArrayToString(words))

	timeStart := time.Now()

	result := removeAnagrams(words)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
