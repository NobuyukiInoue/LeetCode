package solution

import (
	"fmt"
	"strings"
	"time"
)

func countValidWords(sentence string) int {
	// 0ms
	ans, tokens := 0, strings.Fields(sentence)
	for _, token := range tokens {
		count, c, i, b := 0, byte('$'), 0, true
		for j := 0; j < len(token); j++ {
			if token[j] >= '0' && token[j] <= '9' {
				b = false
				break
			}
			if token[j] < 'a' || token[j] > 'z' {
				count++
				if count > 1 {
					if c == '-' && token[j] != '-' && (i > 0 && i < len(token)-1) && j == len(token)-1 && i+1 != j {
						ans++
						b = false
						break
					} else {
						b = false
						break
					}
				}
				c = token[j]
				i = j
			}
		}
		if !b {
			continue
		}
		if c == '$' {
			ans++
		} else if c == '-' {
			if i > 0 && i < len(token)-1 {
				ans++
			}
		} else {
			if i == len(token)-1 {
				ans++
			}
		}
	}
	return ans
}

/*
// bad answer

func countValidWords(sentence string) int {
	result := 0
	s := []rune(sentence)
	var ch rune
	state := 0
	for i := 0; i < len(s); {
		if state == 0 {
			ch = s[i]
			i++
			if ch == ' ' {
				continue
			} else if isLetter(ch) || (isPunctuationMark(ch) && (i == len(s) || s[i] == ' ')) {
				result++
				state = 2
			} else {
				state = 1
			}
		} else if state > 1 {
			ch = s[i]
			state++
			if isDigit(ch) || (ch == '-' && (state == 4 || i == len(s) || !isLetter(s[i]))) || (isPunctuationMark(ch) && i < len(s) && s[i] != ' ') {
				result--
				state = 1
			} else if ch == ' ' {
				state = 0
			}
			i++
		} else if s[i] == ' ' {
			i++
			state = 0
		} else {
			i++
		}
	}
	return result
}

func isLetter(c rune) bool {
	return c >= 'a' && c <= 'z'
}

func isDigit(c rune) bool {
	return c >= '0' && c <= '9'
}

func isPunctuationMark(c rune) bool {
	return c == '!' || c == '.' || c == ','
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	sentence := strings.Replace(temp, "]", "", -1)
	fmt.Printf("sentence = %s\n", sentence)

	timeStart := time.Now()

	result := countValidWords(sentence)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
