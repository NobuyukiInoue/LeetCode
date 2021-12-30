package solution

import (
	"fmt"
	"strings"
	"time"
)

func firstPalindrome(words []string) string {
	// 8ms
	for _, word := range words {
		if check(word) {
			return word
		}
	}
	return ""
}

func check(word string) bool {
	start, end := 0, len(word)-1
	for start < end {
		if word[start] != word[end] {
			return false
		}
		start++
		end--
	}
	return true
}

func firstPalindrome2(words []string) string {
	// 12ms
	for _, word := range words {
		isPalindome := true
		lenWord := len(word)
		for i := 0; i < lenWord/2; i++ {
			if word[i] != word[lenWord-1-i] {
				isPalindome = false
				break
			}
		}
		if isPalindome {
			return word
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := firstPalindrome(words)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
