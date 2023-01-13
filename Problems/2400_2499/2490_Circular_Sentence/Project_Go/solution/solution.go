package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isCircularSentence(sentence string) bool {
	// 0ms
	words := strings.Split(sentence, " ")
	len_words := len(words)
	if words[0][0] != words[len_words-1][len(words[len_words-1])-1] {
		return false
	}
	for i := 0; i < len_words-1; i++ {
		if words[i+1][0] != words[i][len(words[i])-1] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	sentence := strings.Replace(temp, "]", "", -1)
	fmt.Printf("sentence = %s\n", sentence)

	timeStart := time.Now()

	result := isCircularSentence(sentence)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
