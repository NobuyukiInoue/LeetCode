package solution

import (
	"fmt"
	"strings"
	"time"
)

func numOfStrings(patterns []string, word string) int {
	// 0ms
	ans := 0
	for _, pattern := range patterns {
		if strings.Contains(word, pattern) {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	patterns := strings.Split(flds[0], ",")
	word := flds[1]
	fmt.Printf("s = \"%s\", word = \"%s\"\n", patterns, word)

	timeStart := time.Now()

	result := numOfStrings(patterns, word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
