package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortSentence(s string) string {
	// 0ms
	words := strings.Split(s, " ")
	flds := make([]string, len(words))
	for _, word := range words {
		wordLen := len(word)
		flds[word[wordLen-1]-'0'-1] = word[:wordLen-1]
	}
	return strings.Join(flds, " ")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := sortSentence(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
