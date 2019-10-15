package solution

import (
	"bytes"
	"fmt"
	"strings"
	"time"
)

func toGoatLatin(S string) string {
	words := strings.Fields(S)
	vowels := map[byte]bool{
		'a': true, 'A': true,
		'e': true, 'E': true,
		'i': true, 'I': true,
		'o': true, 'O': true,
		'u': true, 'U': true,
	}
	var buffer bytes.Buffer

	for i, word := range words {
		if vowels[word[0]] {
			buffer.WriteString(word)
		} else {
			buffer.WriteString(word[1:])
			buffer.WriteString(string(word[0]))
		}
		buffer.WriteString("ma")
		for j := 1; j <= i+1; j++ {
			buffer.WriteString("a")
		}
		if i != len(words)-1 {
			buffer.WriteString(" ")
		}
	}

	return buffer.String()
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := toGoatLatin(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
