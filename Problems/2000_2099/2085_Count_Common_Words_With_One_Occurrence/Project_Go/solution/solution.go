package solution

import (
	"fmt"
	"strings"
	"time"
)

func countWords(words1 []string, words2 []string) int {
	// 4ms
	dic1 := make(map[string]int)
	dic2 := make(map[string]int)
	for _, word := range words1 {
		dic1[word]++
	}
	for _, word := range words2 {
		dic2[word]++
	}
	ans := 0
	for k, _ := range dic1 {
		if dic1[k] == 1 && dic1[k] == dic2[k] {
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
	word1, word2 := strings.Split(flds[0], ","), strings.Split(flds[1], ",")
	fmt.Printf("word1 = %s, word2 = %s\n", word1, word2)

	timeStart := time.Now()

	result := countWords(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
