package solution

import (
	"fmt"
	"strings"
	"time"
)

func isPrefixOfWord(sentence string, searchWord string) int {
	// 0ms
	words := strings.Split(sentence, " ")
	len_searchWord := len(searchWord)
	for i := 0; i < len(words); i++ {
		if len(words[i]) >= len_searchWord {
			if searchWord == words[i][:len_searchWord] {
				return i + 1
			}
		}
	}

	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	sentence := flds[0]
	searchWord := flds[1]
	fmt.Printf("sentence = \"%s\", searchWord = \"%s\"\n", sentence, searchWord)

	timeStart := time.Now()

	result := isPrefixOfWord(sentence, searchWord)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
