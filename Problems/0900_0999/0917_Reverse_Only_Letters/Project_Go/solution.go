package main

import (
	"fmt"
	"strings"
	"time"
	"unicode"
)

func reverseOnlyLetters(S string) string {
	l, r := 0, len(S)-1
	for l < r {
		runeA := []rune(S)
		if unicode.IsLetter(runeA[l]) && unicode.IsLetter(runeA[r]) {
			runeA[r], runeA[l] = runeA[l], runeA[r]
			S = string(runeA)
			l++
			r--
		} else if unicode.IsLetter(runeA[l]) {
			r--
		} else if unicode.IsLetter(runeA[r]) {
			l++
		} else {
			l++
			r--
		}
	}
	return S
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := reverseOnlyLetters(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
