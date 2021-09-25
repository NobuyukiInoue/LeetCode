package solution

import (
	"fmt"
	"strings"
	"time"
)

func reversePrefix(word string, ch byte) string {
	// 0ms
	pos := strings.Index(word, string(ch))
	if pos >= 0 {
		return string(word[pos]) + reverse(word[:pos]) + word[pos+1:]

	} else {
		return word
	}
}

func reverse(s string) string {
	rs := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	return string(rs)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	word := flds[0]
	ch := flds[1][0]
	fmt.Printf("word = \"%s\", ch = \"%c\"\n", word, ch)

	timeStart := time.Now()

	result := reversePrefix(word, ch)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
