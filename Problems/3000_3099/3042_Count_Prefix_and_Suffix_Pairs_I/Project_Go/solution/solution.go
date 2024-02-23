package solution

import (
	"fmt"
	"strings"
	"time"
)

func countPrefixSuffixPairs(words []string) int {
	// 5ms - 6ms
	ans := 0
	for i := 0; i < len(words)-1; i++ {
		for j := i + 1; j < len(words); j++ {
			if len(words[j]) < len(words[i]) {
				continue
			}
			len_words_i := len(words[i])
			if words[j][:len_words_i] == words[i] && words[j][len(words[j])-len_words_i:] == words[i] {
				ans++
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := countPrefixSuffixPairs(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
