package solution

import (
	"fmt"
	"strings"
	"time"
)

func numMatchingSubseq(S string, words []string) int {
	// 44ms
	res := 0
	sub := make([]string, 0)
	nonsub := make([]string, 0)
	for _, word := range words {
		if contains(sub, word) {
			res++
			continue
		}
		if contains(nonsub, word) {
			continue
		}
		if res == 50 {
			fmt.Print("")
		}
		if isSub(S, word) {
			sub = append(sub, word)
			res++
		} else {
			nonsub = append(nonsub, word)
		}
	}
	return res
}

func contains(words []string, target string) bool {
	for _, word := range words {
		if word == target {
			return true
		}
	}
	return false
}

func isSub(S string, word string) bool {
	pos := 0
	for _, ch := range word {
		index := strings.Index(S[pos:], string(ch))
		pos += index + 1
		if index == -1 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	S := flds[0]
	words := strings.Split(flds[1], ",")
	fmt.Printf("S = %s\n", S)
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := numMatchingSubseq(S, words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
