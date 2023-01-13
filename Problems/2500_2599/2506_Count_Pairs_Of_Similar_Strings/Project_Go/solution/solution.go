package solution

import (
	"fmt"
	"strings"
	"time"
)

func similarPairs(words []string) int {
	// 8ms
	freq := make(map[int]int, 0)
	ans := 0
	for _, word := range words {
		mask := convert(word)
		ans += freq[mask]
		freq[mask]++
	}
	return ans
}

func convert(word string) int {
	n := 0
	for _, ch := range word {
		n |= 1 << (ch - 'a')
	}
	return n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")

	fmt.Printf("words = %s\n", StringArrayToString(words))

	timeStart := time.Now()

	result := similarPairs(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
