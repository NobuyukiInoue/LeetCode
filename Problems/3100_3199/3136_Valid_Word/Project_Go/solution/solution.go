package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isValid(word string) bool {
	// 0ms
	if len(word) < 3 || strings.Contains(word, "@") || strings.Contains(word, "#") || strings.Contains(word, "$") {
		return false
	}
	is_vowel, is_letter := false, false
	word = strings.ToLower(word)
	for _, ch := range word {
		if strings.Contains("aeiou", string(ch)) {
			is_vowel = true
		} else if ch >= 'a' && ch < 'z' {
			is_letter = true
		}
		if is_letter && is_vowel {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := isValid(word)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
